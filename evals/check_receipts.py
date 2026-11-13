"""Check sequential receipt behavior with an isolated fixture worker."""

import argparse
import json
from pathlib import Path
import random
import shutil
import subprocess
import sys
import tempfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import eval_isolation


MAX_FILE_BYTES = 64 * 1024
WORKER = """
import importlib.util
import json
import sys

scenarios = json.load(sys.stdin)
spec = importlib.util.spec_from_file_location('receipts', '/workspace/receipts.py')
receipts = importlib.util.module_from_spec(spec)
spec.loader.exec_module(receipts)
observations = {}
for name, calls in scenarios.items():
    store = receipts.ReceiptStore()
    observations[name] = [
        [receipts.handle(store, tenant, body), list(store.jobs)]
        for tenant, body in calls
    ]
print(json.dumps(observations))
"""


def build_scenarios(seed):
    random_source = random.Random(seed)

    def value(prefix):
        return f"{prefix}-{random_source.getrandbits(64):016x}"

    scenarios = {}
    for index in range(3):
        tenant, other_tenant = value("tenant"), value("tenant")
        key, other_key = value("id"), value("id")
        payload, other_payload = value("payload"), value("payload")
        body = {"request_id": key, "payload": payload}
        different = {"request_id": key, "payload": other_payload}
        scenarios[f"independent_tenants_{index}"] = [
            (tenant, body), (other_tenant, body), (other_tenant, body), (tenant, body)
        ]
        scenarios[f"conflicting_replay_{index}"] = [
            (tenant, body), (tenant, different), (tenant, body)
        ]
        scenarios[f"independent_keys_{index}"] = [
            (tenant, body), (tenant, {"request_id": other_key, "payload": payload}), (tenant, body)
        ]
        scenarios[f"rejected_calls_{index}"] = [
            (None, body), (tenant, {"request_id": "", "payload": payload}),
            (tenant, {"request_id": key}), (tenant, {"request_id": key, "payload": None}),
            (tenant, {"request_id": [key], "payload": payload}), (tenant, None), (tenant, body)
        ]
    return scenarios


def follows_contract(calls, observations):
    if not isinstance(observations, list) or len(calls) != len(observations):
        return False

    receipts = {}
    jobs = []
    for (tenant, body), step in zip(calls, observations):
        if not isinstance(step, list) or len(step) != 2:
            return False
        response, observed_jobs = step
        if not isinstance(response, list) or len(response) != 2:
            return False
        status, data = response
        if type(status) is not int or not isinstance(data, dict):
            return False
        if tenant is None:
            expected = [401, {"error": "unauthenticated"}]
        elif (not isinstance(body, dict) or not isinstance(body.get("request_id"), str)
              or not body["request_id"] or not isinstance(body.get("payload"), str)):
            expected = [400, {"error": "invalid_request"}]
        else:
            key = (tenant, body["request_id"])
            payload = body["payload"]
            if key in receipts:
                original, receipt = receipts[key]
                expected = ([202, {"receipt": receipt}] if payload == original
                            else [409, {"error": "idempotency_conflict"}])
            else:
                receipt = data.get("receipt")
                if not isinstance(receipt, str) or not receipt or any(
                    used == receipt for _, used in receipts.values()
                ):
                    return False
                receipts[key] = (payload, receipt)
                jobs.append([tenant, payload])
                expected = [202, {"receipt": receipt}]
        if response != expected or observed_jobs != jobs:
            return False
    return True


def grade(workspace, seed):
    workspace = workspace.absolute()
    source = workspace / "receipts.py"
    if not eval_isolation.has_direct_path(source) or not source.is_file() or source.stat().st_size > MAX_FILE_BYTES:
        return {"status": "fail", "reason": "Expected a regular receipts.py within the fixture size limit"}

    cases = build_scenarios(seed)
    with tempfile.TemporaryDirectory(prefix="receipt-grader-") as scratch:
        work = Path(scratch)
        shutil.copyfile(source, work / "receipts.py")
        try:
            eval_isolation.probe_offline(work, Path(__file__).resolve(), "receipts.py")
            argv = ["/usr/bin/python3", "-I", "-B", "-c", WORKER]
            with eval_isolation.offline_command(work, argv) as (command, fds):
                with tempfile.TemporaryFile() as output:
                    proc = subprocess.run(command, pass_fds=fds, input=json.dumps(cases).encode(),
                                          stdout=output, stderr=subprocess.DEVNULL, timeout=15)
                    output.seek(0)
                    data = output.read(MAX_FILE_BYTES + 1)
        except subprocess.TimeoutExpired as exc:
            return {"status": "incomplete", "reason": f"Isolation probe or worker timed out ({exc.timeout}s)"}
        except (RuntimeError, OSError, subprocess.CalledProcessError) as exc:
            return {"status": "incomplete", "reason": f"Offline grading unavailable: {type(exc).__name__}"}

    if proc.returncode != 0:
        return {"status": "fail", "reason": f"Fixture worker did not return observations (exit {proc.returncode})"}
    try:
        observed = json.loads(data) if len(data) <= MAX_FILE_BYTES else None
    except (ValueError, RecursionError):
        observed = None
    if not isinstance(observed, dict) or observed.keys() != cases.keys():
        return {"status": "fail", "reason": "Fixture worker returned missing or invalid observations"}
    checks = {name: follows_contract(calls, observed[name]) for name, calls in cases.items()}
    return {"status": "pass" if all(checks.values()) else "fail", "checks": checks}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workspace", type=Path)
    parser.add_argument("--seed", type=int, default=20261113, help="Seed for reproducible evaluator-only inputs")
    args = parser.parse_args()
    result = grade(args.workspace, args.seed)
    print(json.dumps(result))
    return {"pass": 0, "fail": 1, "incomplete": 2}[result["status"]]


if __name__ == "__main__":
    sys.exit(main())

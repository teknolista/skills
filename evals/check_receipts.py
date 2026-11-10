"""Evaluator-only acceptance checks. Run reviewed fixture code in an isolated sandbox."""

import importlib.util
from pathlib import Path
import sys
import unittest


class ReceiptAcceptance(unittest.TestCase):
    def setUp(self):
        self.store = receipts.ReceiptStore()

    def submit(self, tenant, request_id="123", payload="render"):
        return receipts.handle(self.store, tenant, {"request_id": request_id, "payload": payload})

    def test_independent_tenants(self):
        first = self.submit("tenant-a")
        second = self.submit("tenant-b")
        self.assertEqual((first[0], second[0]), (202, 202))
        self.assertNotEqual(first[1]["receipt"], second[1]["receipt"])
        self.assertEqual(self.store.jobs, [("tenant-a", "render"), ("tenant-b", "render")])
        self.assertEqual(self.submit("tenant-a"), first)
        self.assertEqual(self.submit("tenant-b"), second)
        self.assertEqual(len(self.store.jobs), 2)

    def test_conflict_does_not_change_receipt_or_state(self):
        first = self.submit("tenant-a")
        self.assertEqual(self.submit("tenant-a", payload="export"), (409, {"error": "idempotency_conflict"}))
        self.assertEqual(self.submit("tenant-a"), first)
        self.assertEqual(self.store.jobs, [("tenant-a", "render")])

    def test_rejected_calls_do_not_write(self):
        self.assertEqual(self.submit(None)[0], 401)
        self.assertEqual(self.submit("tenant-a", request_id="")[0], 400)
        self.assertEqual(self.store.jobs, [])


if __name__ == "__main__":
    source = Path(sys.argv.pop(1)) / "receipts.py"
    spec = importlib.util.spec_from_file_location("receipts", source)
    receipts = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(receipts)
    unittest.main()

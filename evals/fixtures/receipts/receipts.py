"""Synthetic receipt store and HTTP handler boundary."""


class ReceiptStore:
    def __init__(self):
        self.receipts = {}
        self.jobs = []

    def submit(self, tenant, request_id, payload):
        if request_id in self.receipts:
            return self.receipts[request_id]

        receipt = f"receipt-{len(self.jobs) + 1}"
        self.receipts[request_id] = receipt
        self.jobs.append((tenant, payload))
        return receipt


def handle(store, principal, body):
    if principal is None:
        return 401, {"error": "unauthenticated"}
    if not isinstance(body, dict):
        return 400, {"error": "invalid_request"}
    request_id = body.get("request_id")
    payload = body.get("payload")
    if not isinstance(request_id, str) or not request_id or not isinstance(payload, str):
        return 400, {"error": "invalid_request"}
    return 202, {"receipt": store.submit(principal, request_id, payload)}

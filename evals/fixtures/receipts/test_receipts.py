import unittest

from receipts import ReceiptStore, handle


class ReceiptTests(unittest.TestCase):
    def test_same_tenant_repeat_returns_same_receipt(self):
        store = ReceiptStore()
        body = {"request_id": "123", "payload": "render"}
        status, receipt = handle(store, "tenant-a", body)
        self.assertEqual(status, 202)
        self.assertEqual(handle(store, "tenant-a", body), (202, receipt))
        self.assertEqual(store.jobs, [("tenant-a", "render")])


if __name__ == "__main__":
    unittest.main()

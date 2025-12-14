import hashlib
import json
import time


class Ledger:
    """
    Ledger append-only com hash encadeado.
    """

    def __init__(self):
        self.entries = []
        self.last_hash = "0" * 64

    def append(self, event):
        payload = {
            "timestamp": time.time(),
            "event": event,
            "prev_hash": self.last_hash,
        }

        encoded = json.dumps(payload, sort_keys=True).encode()
        h = hashlib.sha256(encoded).hexdigest()

        payload["hash"] = h
        self.entries.append(payload)
        self.last_hash = h

        return payload

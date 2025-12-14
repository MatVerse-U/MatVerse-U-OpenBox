import json
import hashlib


def replay_and_verify(entries):
    """
    Reexecuta ledger e verifica integridade criptográfica.
    """
    last_hash = "0" * 64

    for entry in entries:
        payload = {
            "timestamp": entry["timestamp"],
            "event": entry["event"],
            "prev_hash": last_hash,
        }

        encoded = json.dumps(payload, sort_keys=True).encode()
        h = hashlib.sha256(encoded).hexdigest()

        if h != entry["hash"]:
            raise RuntimeError("Ledger integrity violation")

        last_hash = h

    return True

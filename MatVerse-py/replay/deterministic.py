import json
import hashlib


def replay_and_verify(entries):
    """
    Reexecuta ledger e verifica integridade criptográfica.
    """
    last_hash = "0" * 64

    for idx, entry in enumerate(entries):
        missing = {k for k in {"timestamp", "event", "hash", "prev_hash"} if k not in entry}
        if missing:
            raise RuntimeError(f"Ledger integrity violation: missing fields {sorted(missing)} at index {idx}")

        if entry["prev_hash"] != last_hash:
            raise RuntimeError(f"Ledger integrity violation: prev_hash mismatch at index {idx}")

        payload = {
            "timestamp": entry["timestamp"],
            "event": entry["event"],
            "prev_hash": entry["prev_hash"],
        }

        encoded = json.dumps(payload, sort_keys=True).encode()
        h = hashlib.sha256(encoded).hexdigest()

        if h != entry["hash"]:
            raise RuntimeError("Ledger integrity violation: hash mismatch")

        last_hash = h

    return True

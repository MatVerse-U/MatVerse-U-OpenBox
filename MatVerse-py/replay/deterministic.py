import json
import hashlib


def _is_hex64(value):
    if not isinstance(value, str):
        return False
    return len(value) == 64 and all(ch in "0123456789abcdef" for ch in value.lower())


def replay_and_verify(entries):
    """
    Reexecuta ledger e verifica integridade criptográfica.
    """
    last_hash = "0" * 64

    for idx, entry in enumerate(entries):
        missing = {k for k in {"timestamp", "event", "hash", "prev_hash"} if k not in entry}
        if missing:
            raise RuntimeError(f"Ledger integrity violation: missing fields {sorted(missing)} at index {idx}")

        if not isinstance(entry["timestamp"], int):
            raise RuntimeError(f"Ledger integrity violation: timestamp must be int at index {idx}")

        if not _is_hex64(entry["hash"]):
            raise RuntimeError(f"Ledger integrity violation: invalid hash format at index {idx}")

        if not _is_hex64(entry["prev_hash"]):
            raise RuntimeError(f"Ledger integrity violation: invalid prev_hash format at index {idx}")

        if entry["prev_hash"] != last_hash:
            raise RuntimeError(f"Ledger integrity violation: prev_hash mismatch at index {idx}")

        payload = {
            "timestamp": entry["timestamp"],
            "event": entry["event"],
            "prev_hash": entry["prev_hash"],
        }

        encoded = json.dumps(
            payload,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
        ).encode("utf-8")
        h = hashlib.sha256(encoded).hexdigest()

        if h != entry["hash"]:
            raise RuntimeError(
                f"Ledger integrity violation: hash mismatch at index {idx} (expected {entry['hash']}, got {h})"
            )

        last_hash = h

    return True

import pytest

from ledger.hashchain import Ledger
from replay.deterministic import replay_and_verify


def test_ledger_replay():
    ledger = Ledger()
    ledger.append({"a": 1})
    ledger.append({"b": 2})

    assert replay_and_verify(ledger.entries) is True


def test_ledger_detects_prev_hash_tampering():
    ledger = Ledger()
    ledger.append({"a": 1})
    ledger.append({"b": 2})

    ledger.entries[1]["prev_hash"] = "1" * 64

    with pytest.raises(RuntimeError):
        replay_and_verify(ledger.entries)


def test_ledger_detects_hash_tampering():
    ledger = Ledger()
    ledger.append({"a": 1})
    ledger.append({"b": 2})

    ledger.entries[0]["event"] = {"a": 999}

    with pytest.raises(RuntimeError):
        replay_and_verify(ledger.entries)


def test_ledger_rejects_non_hex_hashes():
    ledger = Ledger()
    ledger.append({"a": 1})

    ledger.entries[0]["hash"] = "zz" * 32

    with pytest.raises(RuntimeError):
        replay_and_verify(ledger.entries)


def test_ledger_rejects_non_int_timestamp():
    ledger = Ledger()
    ledger.append({"a": 1})

    ledger.entries[0]["timestamp"] = "123"

    with pytest.raises(RuntimeError):
        replay_and_verify(ledger.entries)

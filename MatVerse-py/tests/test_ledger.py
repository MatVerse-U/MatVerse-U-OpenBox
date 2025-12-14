from ledger.hashchain import Ledger
from replay.deterministic import replay_and_verify


def test_ledger_replay():
    ledger = Ledger()
    ledger.append({"a": 1})
    ledger.append({"b": 2})

    assert replay_and_verify(ledger.entries) is True

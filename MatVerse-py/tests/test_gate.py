from omega.gate import omega_gate


def test_allow():
    assert omega_gate(0.05, 0.1, 0.3) == "ALLOW"


def test_block():
    assert omega_gate(0.5, 0.1, 0.3) == "BLOCK"


def test_degrade():
    assert omega_gate(0.15, 0.1, 0.3) == "DEGRADE"

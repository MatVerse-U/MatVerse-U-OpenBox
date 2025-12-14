from omega.cvar import cvar


def test_cvar_basic():
    losses = [0.01, 0.02, 0.5, 0.9]
    v = cvar(losses, alpha=0.75)
    assert v >= 0.5


def test_cvar_zero():
    losses = [0.0, 0.0, 0.0]
    assert cvar(losses) == 0.0

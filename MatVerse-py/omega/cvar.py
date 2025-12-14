import math
from typing import Iterable, List


def _to_vector(values: Iterable[float]) -> List[float]:
    vector = [float(v) for v in values]
    if not vector:
        raise ValueError("losses cannot be empty")
    return vector


def _quantile(vector: List[float], alpha: float) -> float:
    ordered = sorted(vector)
    pos = (len(ordered) - 1) * alpha
    lower = math.floor(pos)
    upper = math.ceil(pos)
    if lower == upper:
        return ordered[lower]
    weight = pos - lower
    return ordered[lower] * (1 - weight) + ordered[upper] * weight


def cvar(losses: Iterable[float], alpha: float = 0.95) -> float:
    """
    Conditional Value at Risk (CVaR).
    Mede risco extremo (cauda), não média.
    """
    if not 0 < alpha < 1:
        raise ValueError("alpha must be in (0,1)")

    vector = _to_vector(losses)
    var = _quantile(vector, alpha)
    tail = [v for v in vector if v >= var]

    if not tail:
        return 0.0

    return sum(tail) / len(tail)

import math
from typing import Callable, Iterable, Tuple


def _to_vector(values: Iterable[float]):
    return [float(v) for v in values]


def _l2_norm(vector):
    return math.sqrt(sum(v * v for v in vector))


def metamorphic_test(model_fn: Callable, x: Iterable[float], perturbation: Iterable[float], tolerance: float = 1e-6) -> Tuple[bool, float]:
    """
    Teste metamórfico:
    pequenas perturbações não devem causar colapso semântico.
    """
    baseline = _to_vector(x)
    delta = _to_vector(perturbation)

    if len(delta) != len(baseline):
        raise ValueError("perturbation must match input dimensionality")

    x_delta = [a + b for a, b in zip(baseline, delta)]

    y1 = _to_vector(model_fn(baseline))
    y2 = _to_vector(model_fn(x_delta))

    if len(y1) != len(y2):
        raise ValueError("model outputs must share dimensionality")

    diff = _l2_norm([a - b for a, b in zip(y1, y2)])

    return diff <= tolerance, diff

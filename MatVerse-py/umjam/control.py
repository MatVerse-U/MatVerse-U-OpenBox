import math
from typing import Iterable, List


def _to_matrix(values: Iterable[Iterable[float]]) -> List[List[float]]:
    matrix = [list(map(float, row)) for row in values]
    if not matrix:
        raise ValueError("K cannot be empty")
    row_len = len(matrix[0])
    if any(len(row) != row_len for row in matrix):
        raise ValueError("K must be a rectangular matrix")
    if row_len != len(matrix):
        raise ValueError("K must be square")
    return matrix


def _to_vector(values: Iterable[float], expected: int | None = None) -> List[float]:
    vector = [float(v) for v in values]
    if expected is not None and len(vector) != expected:
        raise ValueError("theta must match dimensionality of K")
    return vector


def _matvec(matrix: List[List[float]], vector: List[float]) -> List[float]:
    return [sum(a * b for a, b in zip(row, vector)) for row in matrix]


def _identity_minus(matrix: List[List[float]]) -> List[List[float]]:
    size = len(matrix)
    result = []
    for i, row in enumerate(matrix):
        result.append([ (1.0 if i == j else 0.0) - value for j, value in enumerate(row)])
    return result


def _spectral_radius(matrix: List[List[float]], iterations: int = 50) -> float:
    vector = [1.0] * len(matrix)
    radius = 0.0
    for _ in range(iterations):
        vector = _matvec(matrix, vector)
        norm = math.sqrt(sum(v * v for v in vector))
        if norm == 0:
            return 0.0
        vector = [v / norm for v in vector]
        radius = max(radius, norm)
    return radius


class UMJAMController:
    """
    Controle afim externo para governança dinâmica.
    """

    def __init__(self, K: Iterable[Iterable[float]], theta: Iterable[float]):
        self.K = _to_matrix(K)
        self.theta = _to_vector(theta, expected=len(self.K))

        radius = _spectral_radius(self.K)
        if radius >= 1:
            raise ValueError("Unstable controller: lambda_max(K) >= 1")

    def step(self, m: Iterable[float]) -> List[float]:
        metrics = _to_vector(m, expected=len(self.K))
        affine_term = _matvec(self.K, self.theta)
        state_decay = _matvec(_identity_minus(self.K), metrics)
        return [a + b for a, b in zip(state_decay, affine_term)]

"""가까운 수
https://school.programmers.co.kr/tryouts/85945/challenges?language=python3
"""
import pytest
from utils import prvalue


@prvalue(print_result=True)
def solution(array: list[int], n: int) -> int:
    return min(sorted(array), key=lambda x: abs(n - x))


@pytest.mark.parametrize(
    'array, n, expected',
    [
        ([3, 10, 28], 20, 28),
        ([3, 5, 10], 4, 3),
        ([5, 3, 10], 4, 3),
        ([10, 11, 12], 13, 12),
        ([0, 0, 0, 100, 100, 100], 1, 0)
    ]
)
def test_solution(array, n, expected):
    assert solution(array, n) == expected, 'failed'

"""예산
https://school.programmers.co.kr/tryouts/85947/challenges?language=python3
"""
import pytest
from utils import prvalue


@prvalue(print_result=True)
def solution(d: list[int], budget: int) -> int:
    d.sort()
    count, total = 0, budget
    for v in d:
        total -= v
        if total >= 0:
            count += 1

    return count


@prvalue(print_result=True)
def solution2(d: list[int], budget: int) -> int:
    d.sort()
    i = 0
    count = 0
    total = budget
    while i < len(d) and total - d[i] >= 0:
        total -= d[i]
        count += 1
        i += 1

    return count


@pytest.mark.parametrize(
    'd, budget, expected',
    [
        ([1, 3, 2, 5, 4], 9, 3),
        ([2, 2, 3, 3], 10, 4),

    ]
)
def test_solution(d, budget, expected):
    assert solution(d, budget) == expected, 'failed'
    assert solution2(d, budget) == expected, 'failed'

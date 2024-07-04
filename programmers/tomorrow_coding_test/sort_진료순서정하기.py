"""진료 순서 정하기
https://school.programmers.co.kr/tryouts/85946/challenges?language=python3
"""
import pytest
from utils import prvalue


@prvalue(print_result=True)
def solution(emergency: list[int]) -> list[int]:
    sorrted_emergency = sorted(emergency, reverse=True)
    return [sorrted_emergency.index(v) + 1 for v in emergency]


@pytest.mark.parametrize(
    'emergency, expected',
    [
        ([3, 76, 24], [3, 1, 2]),
        ([1, 2, 3, 4, 5, 6, 7], [7, 6, 5, 4, 3, 2, 1]),
        ([30, 10, 23, 6, 100], [2, 4, 3, 5, 1]),
    ]
)
def test_solution(emergency, expected):
    assert solution(emergency) == expected, 'failed'

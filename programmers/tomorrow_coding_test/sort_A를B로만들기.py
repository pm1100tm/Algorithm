"""A를 B로 만들기
https://school.programmers.co.kr/tryouts/85943/challenges?language=python3
"""
import pytest
from utils import prvalue


@prvalue(print_result=True)
def solution(before: str, after: str) -> int:
    return int(sorted(before) == sorted(after))


@pytest.mark.parametrize(
    'before, after, expected',
    [
        ('olleh', 'hello', 1),
        ('allpe', 'apple', 0),
    ]
)
def test_solution(before, after, expected):
    assert solution(before, after) == expected, 'failed'

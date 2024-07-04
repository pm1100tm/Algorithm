"""정렬
https://school.programmers.co.kr/tryouts/85941/challenges?language=python3
"""
import pytest
from utils import prvalue


@prvalue(print_result=True)
def solution(array: list[int], commands: list[list[int]]) -> list[int]:
    """K번째수
    https://school.programmers.co.kr/tryouts/85941/challenges?language=python3
    """
    answer = []
    for com in commands:
        start, end, target = com
        num = sorted(array[start-1:end])[target - 1]
        answer.append(num)

    return answer


@pytest.mark.parametrize(
    'array, commands, expected',
    [
        (
            [1, 5, 2, 6, 3, 7, 4],
            [[2, 5, 3], [4, 4, 1], [1, 7, 3]],
            [5, 6, 3],
        ),
    ]
)
def test_solution(array, commands, expected):
    assert solution(array, commands) == expected, 'failed'

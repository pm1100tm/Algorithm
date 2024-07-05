"""콜라츠 추측
https://school.programmers.co.kr/tryouts/85936/challenges?language=python3
"""
import pytest
from utils import prvalue


@prvalue(print_result=True)
def solution(num: int):
    if num == 1:
        return 0

    n = num
    count = 0
    while n > 1 and count < 500:
        flag: bool = n % 2 == 0
        if flag:
            n = n // 2
        else:
            n = n * 3 + 1

        count += 1

    if count >= 500:
        return -1

    return count


@pytest.mark.parametrize(
    'num, expected',
    [
        (6, 8),
        (16, 4),
        (626331, -1),
        (1, 0),
    ]
)
def test_solution(num: int, expected: int):
    assert solution(num) == expected

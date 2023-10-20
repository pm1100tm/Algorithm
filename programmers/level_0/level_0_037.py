"""
제곱수 판별하기

어떤 자연수를 제곱했을 때 나오는 정수를 제곱수라고 합니다.
정수 n이 매개변수로 주어질 때, n이 제곱수라면 1을 아니라면 2를 return하도록 solution 함수를 완성해주세요.

1 ≤ n ≤ 1,000,000
"""
from typing import Final
from utils import prvalue


@prvalue(print_result=True)
def solution(n: int):
    Y: Final[int] = 1
    N: Final[int] = 2

    root_value = n ** 0.5

    integer_v = int(root_value)
    decimal_v = integer_v - root_value

    if integer_v == 0:
        return 1

    return 1 if decimal_v == 0 else 2


@prvalue()
def solution001(n: int) -> int:
    return 1 if (n ** 0.5).is_integer() else 2


@prvalue()
def solution002(n: int) -> int:
    return 1 if (n ** 0.5) % 1 == 0 else 2


if __name__ == '__main__':
    assert solution(1) == 1
    assert solution(2) == 2
    assert solution(100) == 1
    assert solution(144) == 1
    assert solution(976) == 2
    assert solution(999999) == 2

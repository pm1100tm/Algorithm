"""정수제곱근판별
https://school.programmers.co.kr/learn/courses/30/lessons/12934
"""
from math import sqrt, pow


def solution(n: int) -> int:
    ret = sqrt(n)
    if ret % 1 != 0:
        return -1

    return int(pow(int(ret) + 1, 2))


if __name__ == '__main__':
    assert solution(121) == 144
    assert solution(3) == -1
    assert solution(4) == 9
    assert solution(15) == -1

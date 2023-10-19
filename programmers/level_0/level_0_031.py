"""
자릿수 더하기

정수 n이 매개변수로 주어질 때 n의 각 자리 숫자의 합을 return하도록 solution 함수를 완성해주세요
0 ≤ n ≤ 1,000,000
"""
from functools import reduce
from utils import prvalue


@prvalue()
def solution(n) -> int:
    if n < 10:
        return n

    return reduce(lambda x, y: int(x) + int(y), str(n))


@prvalue()
def solution001(n) -> int:
    return sum([int(_n) for _n in str(n)])


@prvalue()
def solution002(n) -> int:
    answer: int = 0

    while n:
        quo, rem = divmod(n, 10)
        answer += rem
        n = quo

    return answer


if __name__ == '__main__':
    assert solution(0) == 0
    assert solution(1) == 1
    assert solution(10) == 1
    assert solution(9) == 9
    assert solution(1234) == 10
    assert solution(930211) == 16
    assert solution(12345) == 15
    assert solution(12345678999999999) == 117

    assert solution001(0) == 0
    assert solution001(1) == 1
    assert solution001(10) == 1
    assert solution001(9) == 9
    assert solution001(1234) == 10
    assert solution001(930211) == 16
    assert solution001(12345) == 15
    assert solution001(12345678999999999) == 117

    assert solution002(0) == 0
    assert solution002(1) == 1
    assert solution002(10) == 1
    assert solution002(9) == 9
    assert solution002(1234) == 10
    assert solution002(930211) == 16
    assert solution002(12345) == 15
    assert solution002(12345678999999999) == 117

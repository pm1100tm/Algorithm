"""
홀짝에 따라 다른 값 반환하기

한 자리 정수로 이루어진 문자열 num_str이 주어질 때,
각 자리수의 합을 return하도록 solution 함수를 완성해주세요.

3 ≤ num_str ≤ 100
"""
from functools import reduce
from utils import prvalue


@prvalue(print_result=True)
def solution(num_str: str) -> int:
    return reduce(lambda x, y: int(x) + int(y), num_str)


@prvalue()
def solution001(num_str: str) -> int:
    return sum(map(int, list(num_str)))


@prvalue()
def solution002(n: int):
    pass


if __name__ == '__main__':
    assert solution("123456789") == 45
    assert solution("10000000000000000") == 1

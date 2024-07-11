"""N개의 최소공배수
https://school.programmers.co.kr/learn/courses/30/lessons/12953
"""
from utils import prvalue

from math import gcd
from functools import reduce


@prvalue(print_result=True)
def solution(arr: list[int]) -> int:
    def check_lcm(target: int, _arr: list[int]) -> bool:
        return all([target % ele == 0 for ele in _arr])

    max_n = max(arr)
    n, num = 0, 1
    while True:
        n = max_n * num
        if check_lcm(n, arr):
            break
        num += 1

    return n


@prvalue(print_result=True)
def solution2(arr: list[int]) -> int:
    return reduce(lambda acc, cur: acc * cur // gcd(acc, cur), arr, 1)


if __name__ == '__main__':
    assert solution([1,2,3]) == 6
    assert solution([2,6,8,14]) == 168

    assert solution2([1, 2, 3]) == 6
    assert solution2([2,6,8,14]) == 168

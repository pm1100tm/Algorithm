"""
"""
from functools import reduce
from math import prod
from utils import prvalue


@prvalue(print_time=True)
def solution(num_list: list[int]):
    if len(num_list) <= 10:
        return reduce(lambda x, y: x * y, num_list)
    return sum(num_list)


@prvalue(print_time=True)
def solution001(num_list: list[int]):
    if len(num_list) <= 10:
        return prod(num_list)
    return sum(num_list)


@prvalue()
def solution002():
    pass


if __name__ == '__main__':
    assert solution([3, 4, 5, 2, 5, 4, 6, 7, 3, 7, 2, 2, 1]) == 51
    assert solution([2, 3, 4, 5]) == 120

    assert solution001([3, 4, 5, 2, 5, 4, 6, 7, 3, 7, 2, 2, 1]) == 51
    assert solution001([2, 3, 4, 5]) == 120

    n_list = [n for n in range(1, 100000)]

    @prvalue(print_time=True)
    def t1(nl):
        reduce(lambda x, y: x * y, nl)

    @prvalue(print_time=True)
    def t2(nl):
        prod(nl)

    t1(n_list)
    t2(n_list)

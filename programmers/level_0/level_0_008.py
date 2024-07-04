"""짝수의 합
정수 n이 주어질 때, n이하의 짝수를 모두 더한 값을 return 하도록 solution 함수를 작성해주세요.
"""
from utils import prvalue


@prvalue(print_time=True)
def solution001(n: int):
    return sum([number for number in range(n - (n-1), n+1) if number % 2 == 0])


@prvalue(print_time=True)
def solution002(n: int):
    return sum([_n for _n in range(2, n+1, 2)])


if __name__ == '__main__':
    solution001(99999999)
    solution002(99999999)

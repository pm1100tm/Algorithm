"""
공배수

정수 number와 n, m이 주어집니다.
number가 n의 배수이면서 m의 배수이면 1을 아니라면 0을 return하도록 solution 함수를 완성해주세요.
"""
from utils import prvalue


@prvalue()
def solution(number, n, m):
    return int(number % n == 0 and number % m == 0)


@prvalue()
def solution001():
    pass


@prvalue()
def solution002():
    pass


if __name__ == '__main__':
    assert solution(60, 2, 3) == 1
    assert solution(55, 10, 5) == 0

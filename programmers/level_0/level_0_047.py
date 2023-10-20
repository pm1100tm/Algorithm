"""
n의 배수

정수 num과 n이 매개 변수로 주어질 때,
num이 n의 배수이면 1을 return n의 배수가 아니라면 0을 return하도록 solution 함수를 완성해주세요.

2 ≤ num ≤ 100
2 ≤ n ≤ 9
"""
from utils import prvalue


@prvalue()
def solution(num, n) -> int:
    return 1 if 0 == divmod(num, n)[-1] else 0


@prvalue()
def solution001():
    pass


@prvalue()
def solution002():
    pass


if __name__ == '__main__':
    assert solution(98, 2) == 1
    assert solution(34, 3) == 0

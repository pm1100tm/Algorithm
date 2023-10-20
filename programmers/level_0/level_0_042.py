"""
flag에 따라 다른 값 반환하기

두 정수 a, b와 boolean 변수 flag가 매개변수로 주어질 때,
flag가 true면 a + b를 false면 a - b를 return 하는 solution 함수를 작성해 주세요.

-1,000 ≤ a, b ≤ 1,000
"""
from utils import prvalue


@prvalue()
def solution(a: int, b: int, flag: bool) -> int:
    return a + b if flag else a -b


@prvalue()
def solution001():
    pass


@prvalue()
def solution002():
    pass


if __name__ == '__main__':
    assert solution(-4, 7, True) == 3
    assert solution(-4, 7, False) == -11

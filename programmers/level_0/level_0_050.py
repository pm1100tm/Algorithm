"""
홀짝에 따라 다른 값 반환하기

양의 정수 n이 매개변수로 주어질 때, n이 홀수라면 n 이하의 홀수인 모든 양의 정수의 합을 return 하고
n이 짝수라면 n 이하의 짝수인 모든 양의 정수의 제곱의 합을 return 하는 solution 함수를 작성해 주세요.

1 ≤ n ≤ 100
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(n: int) -> int:
    if n % 2 != 0:
        return sum([_n for _n in range(1, n + 1) if _n % 2 != 0])
    return sum([_n**2 for _n in range(1, n + 1) if _n % 2 == 0])


@prvalue()
def solution001(n: int):
    pass


@prvalue()
def solution002(n: int):
    pass


if __name__ == '__main__':
    assert solution(7) == 16
    assert solution(10) == 220

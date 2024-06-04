"""
소수점 아래 숫자가 계속되지 않고 유한개인 소수를 유한소수라고 합니다. 분수를 소수로 고칠 때 유한소수로
나타낼 수 있는 분수인지 판별하려고 합니다. 유한소수가 되기 위한 분수의 조건은 다음과 같습니다.

기약분수로 나타내었을 때, 분모의 소인수가 2와 5만 존재해야 합니다.
두 정수 a와 b가 매개변수로 주어질 때, a/b가 유한소수이면 1을, 무한소수라면 2를 return하도록
solution 함수를 완성해주세요.
"""
from utils import prvalue

import math


def get_prime_factors(n) -> list[int]:
    """
    소인수분해
    """
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    return list(set(factors))


@prvalue(print_result=False)
def solution(a, b):
    # 최대공약수 찾기
    v = math.gcd(a, b)

    # 기약분수의 분모
    x = b // v

    for ele in get_prime_factors(x):
        if ele not in [2, 5]:
            return 2
    return 1


def solution2(a: int, b: int) -> int:
    gcd_val = math.gcd(a, b)
    x = b // gcd_val
    while x % 2 == 0:
        x = x // 2
    while x % 5 == 0:
        x = x // 5

    return 1 if x == 1 else 2


if __name__ == '__main__':
    assert solution(7, 20) == 1
    assert solution(11, 22) == 1
    assert solution(12, 21) == 2

    assert solution2(7, 20) == 1
    assert solution2(11, 22) == 1
    assert solution2(12, 21) == 2

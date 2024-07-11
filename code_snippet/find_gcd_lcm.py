"""최대공약수, 최소공배수
"""
import math
from functools import reduce


def gcd(a: int, b: int) -> int:
    """
    최대공약수: 두 수가 서로 공통으로 가지고 있는 약수 중 가장 큰 수
    """
    return math.gcd(a, b)


def gcd_for_multiple_nums(nums: list[int]) -> int:
    return reduce(lambda x, y: gcd(x, y), nums, 1)


def lcm(a: int, b: int) -> int:
    """
    최소 공배수: 두 수의 공통으로 존재하는 배수 중 가장 작은 수
    """
    return abs(a * b) // gcd(a, b)


if __name__ == '__main__':
    assert gcd(48, 18) == 6
    assert gcd(56, 98) == 14
    assert gcd(123456, 789012) == 12

    assert lcm(2, 7) == 14
    assert lcm(48, 18) == 144
    assert lcm(21, 6) == 42
    assert lcm(123456, 789012) == 8117355456

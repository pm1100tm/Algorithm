"""최대공약수, 최소공배수
"""
import math


def gcd(a: int, b: int) -> int:
    return math.gcd(a, b)


def lcm(a: int, b: int) -> int:
    return abs(a * b) // gcd(a, b)


if __name__ == '__main__':
    assert gcd(48, 18) == 6
    assert gcd(56, 98) == 14
    assert gcd(123456, 789012) == 12

    assert lcm(48, 18) == 144
    assert lcm(21, 6) == 42
    assert lcm(123456, 789012) == 8117355456

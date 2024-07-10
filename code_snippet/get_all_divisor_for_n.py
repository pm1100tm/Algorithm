"""약수 취득하기
"""
import math


def get_all_divisors(n: int) -> list[int]:
    """
    1 is a factor (36 / 1 = 36).
    2 is a factor (36 / 2 = 18).
    3 is a factor (36 / 3 = 12).
    4 is a factor (36 / 4 = 9).
    6 is a factor (36 / 6 = 6).
    """
    divisors = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)

    # need to sort cuz set does not guarantee order and the above operation too
    return sorted(divisors)


if __name__ == '__main__':
    assert get_all_divisors(36) == [1, 2, 3, 4, 6, 9, 12, 18, 36]

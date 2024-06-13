"""콜라문제
"""


def solution(a: int, b: int, n: int):
    total_bottle_got_for_free = 0

    if n < a:
        return total_bottle_got_for_free

    empty_bottle = n

    while empty_bottle >= a:
        quotient, remains = divmod(empty_bottle, a)
        total_bottle_got_for_free += (quotient * b)
        empty_bottle = (quotient * b) + remains

    return total_bottle_got_for_free


if __name__ == '__main__':
    assert solution(2, 1, 20) == 19
    assert solution(3, 1, 20) == 9

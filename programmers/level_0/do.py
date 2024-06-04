import math

from functools import reduce


def prac_reduce():
    t1 = [2, 3, 4, 5]
    t2 = [3, 4, 5, 2, 5, 4, 6, 7, 3, 7, 2, 2, 1]
    assert reduce(lambda x, y: x * y, t1) == 120
    assert reduce(lambda x, y: x * y, t2) == 8467200


def prac_fibonacci(n):
    assert n >= 2
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    print(a, b)
    print(b % 1234567)


if __name__ == '__main__':
    prac_reduce()
    prac_fibonacci(5)

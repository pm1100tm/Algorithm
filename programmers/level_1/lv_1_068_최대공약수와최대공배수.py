"""최대공약수와 최소공배수
https://school.programmers.co.kr/learn/courses/30/lessons/12940
idea: 유클리드 호제법
"""


def solution(n: int, m: int) -> list[int]:
    temp_n = n
    temp_m = m
    gcd = 0

    while m > 0:
        gcd = m
        m = n % m
        n = gcd

    smn = int((temp_n * temp_m) / gcd)

    return [gcd, smn]


def solution2(n: int, m: int) -> list[int]:
    c, d = max(n, m), min(n, m)
    t = 1

    while t > 0:
        t = c % d
        c, d = d, t

    return [c, int(n * m / c)]


if __name__ == '__main__':
    assert solution(3, 12) == [3, 12]
    assert solution(2, 5) == [1, 10]
    assert solution2(3, 12) == [3, 12]
    assert solution2(2, 5) == [1, 10]

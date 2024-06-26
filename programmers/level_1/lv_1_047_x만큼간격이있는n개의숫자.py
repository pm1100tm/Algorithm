"""x만큼 간격이 있는 n개의 숫자
"""


def solution(x: int, n: int) -> list[int]:
    return [i * x + x for i in range(n)]


if __name__ == '__main__':
    assert solution(2, 5) == [2, 4, 6, 8, 10]
    assert solution(4, 3) == [4, 8, 12]
    assert solution(-4, 2) == [-4, -8]

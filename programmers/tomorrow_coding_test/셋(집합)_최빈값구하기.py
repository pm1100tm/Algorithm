"""최빈값 구하기
https://school.programmers.co.kr/tryouts/85922/challenges?language=python3
"""
from collections import Counter


def solution(array: list[int]):
    counter = Counter(array)
    result: list[tuple[int, int]] = counter.most_common()
    if len(result) <= 1:
        return result[0][0]

    if result[0][1] == result[1][1]:
        return -1

    return result[0][0]


if __name__ == '__main__':
    assert solution([1, 2, 3, 3, 3, 4]) == 3
    assert solution([1, 1, 2, 2]) == -1
    assert solution([1]) == 1

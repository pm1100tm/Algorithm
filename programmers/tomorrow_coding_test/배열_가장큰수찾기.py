"""가장 큰 수 찾기
https://school.programmers.co.kr/tryouts/85908/challenges?language=python3
"""


def solution(array: list[int]) -> list[int]:
    max_v = max(array)
    try:
        index = array.index(max_v)
    except IndexError:
        index = 0

    return [max_v, index]


if __name__ == '__main__':
    assert solution([1, 8, 3]) == [8, 1]
    assert solution([9, 10, 11, 8]) == [11, 2]

"""제일작은수제거하기
https://school.programmers.co.kr/learn/courses/30/lessons/12935
"""


def solution(arr: list[int]) -> list[int]:
    if not arr or len(arr) == 1:
        return [-1]

    min_number = min(arr)

    return [n for n in arr if n > min_number]


if __name__ == '__main__':
    assert solution([4, 3, 2, 1]) == [4, 3, 2]
    assert solution([10]) == [-1]

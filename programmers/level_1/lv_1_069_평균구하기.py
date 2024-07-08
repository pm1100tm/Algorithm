"""평균 구하기
https://school.programmers.co.kr/learn/courses/30/lessons/12944
"""


def solution(arr: list[int]) -> float:
    return sum(arr) / len(arr)


if __name__ == '__main__':
    assert solution([1, 2, 3, 4]) == 2.5
    assert solution([5, 5]) == 5

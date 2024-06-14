"""두 개 뽑아서 더하기
https://school.programmers.co.kr/learn/courses/30/lessons/68644?language=python3
"""
from itertools import combinations


def solution(numbers: list[int]) -> list[int]:
    answer = []
    for i in range(len(numbers) - 1):
        answer += [numbers[i] + n for n in numbers[i+1:]]

    answer = list(set(answer))

    return sorted(answer)


def solution2(numbers: list[int]) -> list[int]:
    n_list = [
        a + b
        for a, b in combinations(numbers, 2)
    ]

    answer = list(set(n_list))
    answer.sort()

    return answer


if __name__ == '__main__':
    assert solution([2, 1, 3, 4, 1]) == [2, 3, 4, 5, 6, 7]
    assert solution([5,0,2,7]) == [2,5,7,9,12]
    assert solution2([2,1,3,4,1]) == [2, 3, 4, 5, 6, 7]
    assert solution2([5,0,2,7]) == [2,5,7,9,12]

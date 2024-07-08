"""행렬의 덧셈
https://school.programmers.co.kr/learn/courses/30/lessons/12950
"""


def solution(arr1: list[list[int]], arr2: list[list[int]]) -> list[list[int]]:
    answer = [[] for _ in range(len(arr2))]
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            answer[i].append(arr1[i][j] + arr2[i][j])

    return answer


def solution2(arr1: list[list[int]], arr2: list[list[int]]) -> list[list[int]]:
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(arr1, arr2)]
    return answer


if __name__ == '__main__':
    assert solution([[1, 2], [2, 3]], [[3, 4], [5, 6]]) == [[4, 6], [7, 9]]
    assert solution([[1], [2]], [[3], [4]]) == [[4], [6]]
    assert solution2([[1, 2], [2, 3]], [[3, 4], [5, 6]]) == [[4, 6], [7, 9]]
    assert solution2([[1], [2]], [[3], [4]]) == [[4], [6]]

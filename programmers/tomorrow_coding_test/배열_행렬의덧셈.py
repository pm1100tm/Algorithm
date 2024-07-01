"""행렬의덧셈
https://school.programmers.co.kr/tryouts/85910/challenges?language=python3
"""


def solution(arr1: list[list[int]], arr2: list[list[int]]) -> list[list[int]]:
    i = len(arr1[0])
    answer = []
    for v1, v2 in zip(arr1, arr2):
        n_list = [v1[j] + v2[j] for j in range(i)]
        answer.append(n_list)

    return answer


if __name__ == '__main__':
    assert solution([[1,2],[2,3]], [[3,4],[5,6]]) == [[4, 6], [7, 9]]
    assert solution([[1],[2]], [[3], [4]]) == [[4],[6]]

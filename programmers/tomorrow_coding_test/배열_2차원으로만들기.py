"""2차원으로 만들기
https://school.programmers.co.kr/tryouts/85906/challenges?language=python3
"""


def solution(num_list: list[int], n: int) -> list[list[int]]:
    answer = []
    for i in range(0, len(num_list) // n):
        answer.append(num_list[i * n: i * n + n])

    return answer


if __name__ == '__main__':
    assert (
        solution([1, 2, 3, 4, 5, 6, 7, 8], 2)
    ) == [[1, 2], [3, 4], [5, 6], [7, 8]]
    assert (
        solution([100, 95, 2, 4, 5, 6, 18, 33, 948], 3)
    ) == [[100, 95, 2], [4, 5, 6], [18, 33, 948]]


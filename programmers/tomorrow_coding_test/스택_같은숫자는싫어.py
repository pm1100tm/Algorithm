"""같은 숫자는 싫어
https://school.programmers.co.kr/tryouts/85927/challenges?language=python3
"""


def solution(arr: list[int]) -> list[int]:
    answer = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            answer.append(arr[i])

    return answer


if __name__ == '__main__':
    assert solution([1,1,3,3,0,1,1]) == [1,3,0,1]
    assert solution([4,4,4,3,3]) == [4, 3]

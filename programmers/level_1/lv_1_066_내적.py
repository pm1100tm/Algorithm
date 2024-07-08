"""내적
https://school.programmers.co.kr/learn/courses/30/lessons/70128
"""


def solution(a: list[int], b: list[int]):
    if len(a) == 1:
        return a[-1] * b[-1]

    answer = 0
    for index in range(len(a)):
        answer += a[index] * b[index]

    return answer


if __name__ == '__main__':
    assert solution([1,2,3,4], [-3,-1,0,2]) == 3
    assert solution([-1,0,1], [1,0,-1]) == -2

"""약수의 합
https://school.programmers.co.kr/learn/courses/30/lessons/12928
"""


def solution(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 1

    answer = n + 1
    _n = 2
    while _n <= n // 2:
        if n % _n == 0:
            answer += _n
        _n += 1

    return answer


if __name__ == '__main__':
    solution(12)
    solution(5)

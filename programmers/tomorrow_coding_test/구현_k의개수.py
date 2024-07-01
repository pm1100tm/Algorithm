"""k의 개수
https://school.programmers.co.kr/tryouts/85901/challenges?language=python3
"""


def solution(i, j, k):
    num_string = ''.join([str(n) for n in range(i, j + 1)])
    return num_string.count(str(k))


if __name__ == '__main__':
    assert solution(1, 13, 1) == 6
    assert solution(10, 50, 5) == 5
    assert solution(3, 10, 2) == 0

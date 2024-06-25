"""정수 내림차순으로 배치하기
https://school.programmers.co.kr/learn/courses/30/lessons/12933
"""


def solution(n: int):
    return int(''.join(sorted(str(n), reverse=True)))


if __name__ == '__main__':
    assert solution(118372) == 873211

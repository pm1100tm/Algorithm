"""7의 개수
https://school.programmers.co.kr/tryouts/85907/challenges?language=python3
"""


def solution(array: list[int]) -> int:
    return ''.join([str(v) for v in array]).count('7')


if __name__ == '__main__':
    assert solution([7, 77, 17]) == 4
    assert solution([10, 29]) == 0

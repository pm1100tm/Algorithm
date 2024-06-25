"""문자열을 정수로 바꾸기
https://school.programmers.co.kr/learn/courses/30/lessons/12925?language=python3
"""


def solution(s) -> int:
    return int(s)


if __name__ == '__main__':
    assert solution('-1') == -1
    assert solution('-12345') == -12345
    assert solution('54321') == 54321
    assert solution('321') == 321
    assert solution('-321') == -321

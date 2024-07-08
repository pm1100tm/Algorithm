"""이진 변환 반복하기
https://school.programmers.co.kr/learn/courses/30/lessons/70129
"""
from utils import prvalue


def decimal_to_binary(n: int) -> str:
    if n == 0:
        return "0"

    binary_str = ""
    while n > 0:
        binary_str = str(n % 2) + binary_str
        n = n // 2

    return binary_str


@prvalue(print_result=True)
def solution(s: str) -> list[int]:
    int_chars = s
    n, r = 0, 0
    while int_chars != '1':
        r += int_chars.count('0')
        int_chars = int_chars.replace('0', '')
        int_chars = decimal_to_binary(len(int_chars))
        n += 1

    return [n, r]


if __name__ == '__main__':
    assert solution('110010101001') == [3, 8]
    assert solution('01110') == [3, 8]
    assert solution('1111111') == [3, 8]

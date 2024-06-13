"""
진수 변경하기
"""


def convert_number_formation_with_n(number: int, n: int) -> str:
    if n == 0:
        return '0'

    result = ''
    while number > 0:
        remainder = number % n
        result += str(remainder)
        number //= n

    return result

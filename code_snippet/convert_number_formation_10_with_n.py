"""
10진수를 특정 진수로 변경하기
"""
from utils import prvalue


@prvalue(print_result=True)
def convert_number_formation_with_n(number: int, n: int) -> str:
    if n == 0:
        return '0'
    if n == 10:
        return str(number)

    result = ''
    while number > 0:
        remainder = number % n
        result += str(remainder)
        number //= n

    return result


@prvalue(print_result=True)
def decimal_to_binary(n: int) -> str:
    if n == 0:
        return "0"

    binary_str = ""
    while n > 0:
        binary_str = str(n % 2) + binary_str
        n = n // 2

    return binary_str


if __name__ == '__main__':
    assert convert_number_formation_with_n(10, 2) == '0101'
    assert convert_number_formation_with_n(10, 3) == '101'
    assert convert_number_formation_with_n(10, 10) == '10'
    assert decimal_to_binary(4) == '100'

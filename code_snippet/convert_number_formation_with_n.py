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


if __name__ == '__main__':
    assert convert_number_formation_with_n(10, 2) == '0101'
    assert convert_number_formation_with_n(10, 3) == '101'
    assert convert_number_formation_with_n(10, 10) == '10'

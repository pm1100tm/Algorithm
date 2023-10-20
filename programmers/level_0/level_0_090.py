"""
인덱스 바꾸기

문자열 my_string과 정수 num1, num2가 매개변수로 주어질 때,
my_string에서 인덱스 num1과 인덱스 num2에 해당하는 문자를 바꾼 문자열을 return 하도록
solution 함수를 완성해보세요.

1 < my_string의 길이 < 100
0 ≤ num1, num2 < my_string의 길이
my_string은 소문자로 이루어져 있습니다.
num1 ≠ num2

"hello"	1	2	"hlelo"
"I love you"	3	6	"I l veoyou"
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(my_string: str, num1: int, num2: int) -> str:
    _my_string = list(my_string)
    _my_string[num2], _my_string[num1] = _my_string[num1], _my_string[num2]

    return "".join(_my_string)


if __name__ == '__main__':
    solution("hello", 1, 2)
    solution("I love you", 3, 6)

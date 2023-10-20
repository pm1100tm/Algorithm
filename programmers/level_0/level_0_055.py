"""
문자열의 뒤의 n글자

문자열 my_string과 정수 n이 매개변수로 주어질 때,
my_string의 뒤의 n글자로 이루어진 문자열을 return 하는 solution 함수를 작성해 주세요.

my_string은 숫자와 알파벳으로 이루어져 있습니다.
1 ≤ my_string의 길이 ≤ 1,000
1 ≤ n ≤ my_string의 길이
"""
from utils import prvalue


@prvalue()
def solution(my_string: str, n: int) -> str:
    # return my_string[-1*n:]
    return my_string[-n:]


@prvalue()
def solution001():
    pass


@prvalue()
def solution002():
    pass


if __name__ == '__main__':
    assert solution("ProgrammerS123", 11) == "grammerS123"
    assert solution("He110W0r1d", 5) == "W0r1d"

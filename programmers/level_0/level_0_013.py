"""
문자열 뒤집기

문자열 my_string이 매개변수로 주어집니다.
my_string을 거꾸로 뒤집은 문자열을 return하도록 solution 함수를 완성해주세요.
"""
from utils import prvalue


@prvalue()
def solution001(my_string: str) -> str:
    return my_string[::-1]


if __name__ == '__main__':
    solution001("jaron")
    solution001("bread")

"""
소문자로 바꾸기

알파벳으로 이루어진 문자열 myString이 주어집니다.
모든 알파벳을 소문자로 변환하여 return 하는 solution 함수를 완성해 주세요.
"""
from utils import prvalue


@prvalue()
def solution(my_string: str) -> str:
    return my_string.lower()


@prvalue()
def solution001():
    pass


@prvalue()
def solution002():
    pass


if __name__ == '__main__':
    solution()
    solution001()
    solution002()

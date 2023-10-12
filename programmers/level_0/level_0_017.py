"""
특정 문자 제거하기

문자열 my_string과 문자 letter이 매개변수로 주어집니다.
my_string에서 letter를 제거한 문자열을 return하도록 solution 함수를 완성해주세요.
"""
from utils import prvalue


@prvalue()
def solution001(my_string: str, letter: str) -> str:
    return my_string.replace(letter, "")


@prvalue()
def solution002(my_string: str, letter: str) -> str:
    import re
    return re.sub(re.escape(letter), '', my_string)


@prvalue()
def solution003(my_string: str, letter: str) -> str:
    return "".join([s for s in my_string if s != letter])

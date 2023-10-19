"""
문자열안에 문자열

문자열 str1, str2가 매개변수로 주어집니다.
str1 안에 str2가 있다면 1을 없다면 2를 return하도록 solution 함수를 완성해주세요.
"""
from utils import prvalue


@prvalue()
def solution001(str1: str, str2: str) -> int:
    return 1 if str2 in str1 else 2


@prvalue()
def solution002(str1: str, str2: str) -> int:
    return 1 + (str2 not in str1)


@prvalue()
def solution003(str1: str, str2: str) -> int:
    return 1 if str1.find(str2) >= 0 else 2

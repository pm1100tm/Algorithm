"""
배열 원소의 길이

문자열 배열 strlist가 매개변수로 주어집니다.
strlist 각 원소의 길이를 담은 배열을 retrun하도록 solution 함수를 완성해주세요.
"""
from utils import prvalue


@prvalue()
def solution001(strlist: list[str]) -> list[int]:
    return [len(s) for s in strlist]


@prvalue()
def solution002(strlist: list[str]) -> list[int]:
    return list(map(len, strlist))

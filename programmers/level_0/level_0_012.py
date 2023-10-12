"""
배열 뒤집기

정수가 들어 있는 배열 num_list가 매개변수로 주어집니다.
num_list의 원소의 순서를 거꾸로 뒤집은 배열을 return하도록 solution 함수를 완성해주세요.
"""
from utils import prvalue


@prvalue()
def solution001(num_list: list[int]) -> list[int]:
    return num_list[::-1]


@prvalue()
def solution002(num_list: list[int]) -> list[int]:
    result: list[int] = []
    while num_list:
        result.append(num_list.pop())

    return result

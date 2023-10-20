"""
카운트 업

정수 start_num와 end_num가 주어질 때, start_num부터 end_num까지의 숫자를
차례로 담은 리스트를 return하도록 solution 함수를 완성해주세요.

0 ≤ start_num ≤ end_num ≤ 50
"""
from utils import prvalue


@prvalue()
def solution(start_num: int, end_num: int) -> list[int]:
    return [v for v in range(start_num, end_num + 1)]


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

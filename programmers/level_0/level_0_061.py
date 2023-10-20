"""
카운트 다운

정수 start_num와 end_num가 주어질 때,
start_num에서 end_num까지 1씩 감소하는 수들을 차례로 담은 리스트를 return하도록
solution 함수를 완성해주세요.
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(start: int, end_num: int) -> list[int]:
    return [n for n in range(start, end_num - 1, -1)]


@prvalue()
def solution001(start: int, end_num: int) -> list[int]:
    return [start - n for n in range(start - end_num + 1)]


@prvalue()
def solution002():
    pass


if __name__ == '__main__':
    assert solution(10, 3) == [10, 9, 8, 7, 6, 5, 4, 3]
    assert solution001(10, 3) == [10, 9, 8, 7, 6, 5, 4, 3]

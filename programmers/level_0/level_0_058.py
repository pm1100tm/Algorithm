"""
n개 간격의 원소들

정수 리스트 num_list와 정수 n이 주어질 때,
num_list의 첫 번째 원소부터 마지막 원소까지 n개 간격으로 저장되어있는 원소들을 차례로 담은
리스트를 return하도록 solution 함수를 완성해주세요.
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(num_list: list[int], n: int):
    return num_list[::n]


@prvalue()
def solution001():
    pass


@prvalue()
def solution002():
    pass


if __name__ == '__main__':
    assert solution([], 2) == []
    assert solution([1], 2) == [1]
    assert solution([1], 1) == [1]
    assert solution([1, 3], 2) == [1]
    assert solution([4, 2, 6, 1, 7, 6], 2) == [4, 6, 7]
    assert solution([4, 2, 6, 1, 7, 6], 4) == [4, 7]

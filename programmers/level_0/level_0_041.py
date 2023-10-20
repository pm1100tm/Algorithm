"""
n 번째 원소까지

정수 리스트 num_list와 정수 n이 주어질 때,
num_list의 첫 번째 원소부터 n 번째 원소까지의 모든 원소를 담은 리스트를 return하도록
solution 함수를 완성해주세요.

2 ≤ num_list의 길이 ≤ 30
1 ≤ num_list의 원소 ≤ 9
1 ≤ n ≤ num_list의 길이 ___
"""
from utils import prvalue


@prvalue()
def solution(num_list: list[int], n: int):
    return num_list[:n]


@prvalue()
def solution001():
    pass


@prvalue()
def solution002():
    pass


if __name__ == '__main__':
    assert solution([2, 1, 6], 1) == [2]
    assert solution([5, 2, 1, 7, 5], 3) == [5, 2, 1]

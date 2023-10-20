"""
순서 바꾸기

정수 리스트 num_list와 정수 n이 주어질 때,
num_list를 n 번째 원소 이후의 원소들과 n 번째까지의 원소들로 나눠
n 번째 원소 이후의 원소들을 n 번째까지의 원소들 앞에 붙인 리스트를 return하도록
solution 함수를 완성해주세요.

2 ≤ num_list의 길이 ≤ 30
1 ≤ num_list의 원소 ≤ 9
1 ≤ n ≤ num_list의 길이

[2, 1, 6]	1	[1, 6, 2]
[5, 2, 1, 7, 5]	3	[7, 5, 5, 2, 1]
"""
from collections import deque
from utils import prvalue


@prvalue(print_time=True)
def solution(num_list: list[int], n: int) -> list[int]:
    return num_list[n:] + num_list[:n]


@prvalue(print_time=True)
def solution001(num_list: list[int], n: int) -> list[int]:
    num_list_deque = deque(num_list)
    num_list_deque.rotate(-n)
    return list(num_list_deque)


if __name__ == '__main__':
    assert solution([2, 1, 6], 1) == [1, 6, 2]
    assert solution([5, 2, 1, 7, 5], 3) == [7, 5, 5, 2, 1]
    assert solution001([2, 1, 6], 1) == [1, 6, 2]
    assert solution001([5, 2, 1, 7, 5], 3) == [7, 5, 5, 2, 1]

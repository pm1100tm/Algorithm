"""
정수 찾기

정수 리스트 num_list와 찾으려는 정수 n이 주어질 때,
num_list안에 n이 있으면 1을 없으면 0을 return하도록 solution 함수를 완성해주세요.

3 ≤ num_list의 길이 ≤ 100
1 ≤ num_list의 원소 ≤ 100
1 ≤ n ≤ 100

[1, 2, 3, 4, 5] 안에 3이 있으므로 1을 return합니다.
[15, 98, 23, 2, 15] 안에 20이 없으므로 0을 return합니다.
"""
from utils import prvalue


@prvalue()
def solution(num_list: list[int], n: int) -> int:
    return int(n in num_list)


@prvalue()
def solution001():
    pass


@prvalue()
def solution002():
    pass


if __name__ == '__main__':
    assert solution([1, 2, 3, 4, 5], 3) == 1
    assert solution([15, 98, 23, 2, 15], 20) == 0

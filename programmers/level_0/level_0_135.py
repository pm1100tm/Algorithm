"""
2의 영역

정수 배열 arr가 주어집니다.
배열 안의 2가 모두 포함된 가장 작은 연속된 부분 배열을 return 하는 solution 함수를 완성해 주세요.
단, arr에 2가 없는 경우 [-1]을 return 합니다.

1 ≤ arr의 길이 ≤ 100,000
1 ≤ arr의 원소 ≤ 10

[1, 2, 1, 4, 5, 2, 9]	[2, 1, 4, 5, 2]
[1, 2, 1]	[2]
[1, 1, 1]	[-1]
[1, 2, 1, 2, 1, 10, 2, 1]
[1, 2, 1, 2, 1, 10, 2, 1]	[2, 1, 2, 1, 10, 2]
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(arr: list[int]):
    if 2 not in arr:
        return [-1]
    s, e = 0, 0
    for i, n in enumerate(arr, 1):
        if n == 2:
            if not s:
                s = i
                e = i
            else:
                e = i

    return arr[s - 1: e]


@prvalue(print_result=True)
def solution001(arr: list[int]):
    if 2 not in arr:
        return [-1]

    return arr[arr.index(2) : len(arr) - arr[::-1].index(2)]


if __name__ == '__main__':
    assert solution([1, 2, 1, 4, 5, 2, 9]) == [2, 1, 4, 5, 2]
    assert solution([1, 2, 1]) == [2]
    assert solution([1, 1, 1]) == [-1]
    assert solution([1, 2, 1, 2, 1, 10, 2, 1]) == [2, 1, 2, 1, 10, 2]
    assert solution([2, 1, 1, 2, 1, 10, 12390, 1]) == [2, 1, 1, 2]

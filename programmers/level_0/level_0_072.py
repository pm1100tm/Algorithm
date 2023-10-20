"""
배열 비교하기

이 문제에서 두 정수 배열의 대소관계를 다음과 같이 정의합니다.
두 배열의 길이가 다르다면, 배열의 길이가 긴 쪽이 더 큽니다.
배열의 길이가 같다면 각 배열에 있는 모든 원소의 합을 비교하여 다르다면 더 큰 쪽이 크고, 같다면 같습니다.
두 정수 배열 arr1과 arr2가 주어질 때, 위에서 정의한 배열의 대소관계에 대하여 arr2가 크다면 -1,
arr1이 크다면 1, 두 배열이 같다면 0을 return 하는 solution 함수를 작성해 주세요.

1 ≤ arr1의 길이 ≤ 100
1 ≤ arr2의 길이 ≤ 100
1 ≤ arr1의 원소 ≤ 100
1 ≤ arr2의 원소 ≤ 100

[49, 13]	[70, 11, 2]	-1
[100, 17, 84, 1]	[55, 12, 65, 36]	1
[1, 2, 3, 4, 5]	[3, 3, 3, 3, 3]	0
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(arr1: list[int], arr2: list[int]) -> int:
    R1, R2, R3 = 1, -1, 0
    len_arr1, len_arr2 = len(arr1), len(arr2)
    if len_arr1 != len_arr2:
        return R1 if len_arr1 > len_arr2 else R2

    sum1, sum2 = sum(arr1), sum(arr2)
    if sum1 == sum2:
        return R3
    else:
        return R1 if sum1 > sum2 else R2


if __name__ == '__main__':
    assert solution([49, 13], [70, 11, 2]) == -1
    assert solution([100, 17, 84, 1], [55, 12, 65, 36]) == 1
    assert solution([1, 2, 3, 4, 5], [3, 3, 3, 3, 3]) == 0

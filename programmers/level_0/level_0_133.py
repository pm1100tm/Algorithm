"""
배열의 길이를 2의 거듭제곱으로 만들기

정수 배열 arr이 매개변수로 주어집니다.
arr의 길이가 2의 정수 거듭제곱이 되도록 arr 뒤에 정수 0을 추가하려고 합니다.
arr에 최소한의 개수로 0을 추가한 배열을 return 하는 solution 함수를 작성해 주세요.

1 ≤ arr의 길이 ≤ 1,000
1 ≤ arr의 원소 ≤ 1,000

[1, 2, 3, 4, 5, 6]	[1, 2, 3, 4, 5, 6, 0, 0]
[58, 172, 746, 89]	[58, 172, 746, 89]
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(arr):
    len_arr = len(arr)
    multiple_number = 0
    while True:
        v = 2 ** multiple_number
        if len_arr > v:
            multiple_number += 1
            continue
        arr += [0] * (v - len_arr)
        break

    return arr


@prvalue(print_result=True)
def solution001(arr):
    a, b = 1, len(arr)
    while a < b :
        a *= 2

    return arr + [0] * (a-b)


if __name__ == '__main__':
    assert solution([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6, 0, 0]
    assert solution([58, 172, 746, 89]) == [58, 172, 746, 89]
    assert solution([58, 172, 746, 89, 1, 1, 1, 1]) == [58, 172, 746, 89, 1, 1, 1, 1]
    assert solution([1]) == [1]
    assert solution([1, 2]) == [1, 2]

"""
배열의 길이에 따라 다른 연산하기

정수 배열 arr과 정수 n이 매개변수로 주어집니다.
arr의 길이가 홀수라면 arr의 모든 짝수 인덱스 위치에 n을 더한 배열을,
arr의 길이가 짝수라면 arr의 모든 홀수 인덱스 위치에 n을 더한 배열을
return 하는 solution 함수를 작성해 주세요.

1 ≤ arr의 길이 ≤ 1,000
1 ≤ arr의 원소 ≤ 1,000
1 ≤ n ≤ 1,000
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(arr: list[int], n: int) -> list[int]:
    is_odd = len(arr) % 2 != 0
    plus_n = lambda x: x + n
    return [
        plus_n(number) if index % 2 != is_odd else number
        for index, number in enumerate(arr)
    ]


@prvalue(print_result=True)
def solution001(arr: list[int], n: int) -> list[int]:
    length = len(arr)
    is_odd = length % 2 != 0
    start_index: int = 0 if is_odd else 1

    for i in range(start_index, length, 2):
        arr[i] += n

    return arr


if __name__ == '__main__':
    assert solution([49, 12, 100, 276, 33], 27) == [76, 12, 127, 276, 60]
    assert solution([444, 555, 666, 777], 100) == [444, 655, 666, 877]

    assert solution001([49, 12, 100, 276, 33], 27)
    assert solution001([444, 555, 666, 777], 100)

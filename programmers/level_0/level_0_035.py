"""
중앙값 구하기

중앙값은 어떤 주어진 값들을 크기의 순서대로 정렬했을 때 가장 중앙에 위치하는 값을 의미합니다.
예를 들어 1, 2, 7, 10, 11의 중앙값은 7입니다.
정수 배열 array가 매개변수로 주어질 때, 중앙값을 return 하도록 solution 함수를 완성해보세요.

array의 길이는 홀수입니다.
0 < array의 길이 < 100
-1,000 < array의 원소 < 1,000
"""
from utils import prvalue


@prvalue()
def solution(array: list[int]) -> int:
    array.sort()
    length = len(array)
    index = int(length / 2)
    if length % 2 == 0:
        index += 1

    return array[index]


@prvalue()
def solution001(array: list[int]) -> int:
    return sorted(array)[len(array) // 2]


if __name__ == '__main__':
    assert solution([1, 2, 7, 10, 11]) == 7
    assert solution([9, -1, 0]) == 0

    assert solution001([1, 2, 7, 10, 11]) == 7
    assert solution001([9, -1, 0]) == 0

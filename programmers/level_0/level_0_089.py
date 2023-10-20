"""
가장 큰 수 찾기

정수 배열 array가 매개변수로 주어질 때,
가장 큰 수와 그 수의 인덱스를 담은 배열을 return 하도록 solution 함수를 완성해보세요.

1 ≤ array의 길이 ≤ 100
0 ≤ array 원소 ≤ 1,000
array에 중복된 숫자는 없습니다.

[1, 8, 3]	[8, 1]
[9, 10, 11, 8]	[11, 2]
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(array: list[int]) -> list[int]:
    max_num = sorted(array)[-1]
    index = array.index(max_num)
    return [max_num, index]


@prvalue(print_result=True)
def solution001(array: list[int]) -> list[int]:
    max_num = max(array)
    return [max_num, array.index(max_num)]


if __name__ == '__main__':
    assert solution([1, 8, 3]) == [8, 1]
    assert solution([9, 10, 11, 8]) == [11, 2]

    assert solution001([1, 8, 3]) == [8, 1]
    assert solution001([9, 10, 11, 8]) == [11, 2]

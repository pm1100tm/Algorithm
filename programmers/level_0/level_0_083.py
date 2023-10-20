"""
최댓값 만들기 (2)

정수 배열 numbers가 매개변수로 주어집니다.
numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.

제한사항
-10,000 ≤ numbers의 원소 ≤ 10,000
2 ≤ numbers 의 길이 ≤ 100

[1, 2, -3, 4, -5]	15
[0, -31, 24, 10, 1, 9]	240
[10, 20, 30, 5, 5, 20, 5]	600
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(numbers: list[int]) -> int:
    numbers.sort()
    n1 = numbers[0] * numbers[1]
    n2 = numbers[-1] * numbers[-2]
    return max(n1, n2)


@prvalue(print_result=True)
def solution001(numbers: list[int]) -> int:
    from itertools import combinations as comb
    return max([i * j for i, j in comb(numbers, 2)])


if __name__ == '__main__':
    assert solution([1, 2, -3, 4, -5]) == 15
    assert solution([0, -31, 24, 10, 1, 9]) == 240
    assert solution([10, 20, 30, 5, 5, 20, 5]) == 600

    assert solution001([1, 2, -3, 4, -5]) == 15
    assert solution001([0, -31, 24, 10, 1, 9]) == 240
    assert solution001([10, 20, 30, 5, 5, 20, 5]) == 600

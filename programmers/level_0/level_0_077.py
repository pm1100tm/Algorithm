"""
n의 배수 고르기

정수 n과 정수 배열 numlist가 매개변수로 주어질 때,
numlist에서 n의 배수가 아닌 수들을 제거한 배열을 return하도록 solution 함수를 완성해주세요.

1 ≤ n ≤ 10,000
1 ≤ numlist의 크기 ≤ 100
1 ≤ numlist의 원소 ≤ 100,000
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(n, numlist) -> list[int]:
    by_n_list = [_n for _n in range(0, 10000 + 1, n)]
    return [num for num in numlist if num in by_n_list]


if __name__ == '__main__':
    solution(3, [4, 5, 6, 7, 8, 9, 10, 11, 12])
    solution(5, [1, 9, 3, 10, 13, 5])
    solution(12, [2, 100, 120, 600, 12, 12])

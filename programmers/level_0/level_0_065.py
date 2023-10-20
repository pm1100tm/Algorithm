"""
배열 만들기 1

정수 n과 k가 주어졌을 때, 1 이상 n이하의 정수 중에서 k의 배수를 오름차순으로 저장한 배열을
return 하는 solution 함수를 완성해 주세요.

1 ≤ n ≤ 1,000,000
1 ≤ k ≤ min(1,000, n)
"""
from utils import prvalue


@prvalue()
def solution(n: int, k: int):
    return [num for num in range(k, n + 1, k)]


if __name__ == '__main__':
    assert solution(10, 3) == [3, 6, 9]
    assert solution(15, 5) == [5, 10, 15]

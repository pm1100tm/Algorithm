"""
가까운 수

정수 배열 array와 정수 n이 매개변수로 주어질 때,
array에 들어있는 정수 중 n과 가장 가까운 수를 return 하도록 solution 함수를 완성해주세요.

1 ≤ array의 길이 ≤ 100
1 ≤ array의 원소 ≤ 100
1 ≤ n ≤ 100
가장 가까운 수가 여러 개일 경우 더 작은 수를 return 합니다.

[3, 10, 28]	20	28
[10, 11, 12]	13	12
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(array, n):
    return min(sorted(array), key=lambda x: abs(n-x))


if __name__ == '__main__':
    assert solution([3, 10, 28, 12], 20) == 12
    assert solution([10, 11, 12], 13) == 12
    assert solution([4, 2, 12], 3) == 2

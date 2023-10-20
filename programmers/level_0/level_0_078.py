"""
홀수 vs 짝수

정수 리스트 num_list가 주어집니다.
가장 첫 번째 원소를 1번 원소라고 할 때,
홀수 번째 원소들의 합과 짝수 번째 원소들의 합 중 큰 값을 return 하도록 solution 함수를 완성해주세요.
두 값이 같을 경우 그 값을 return합니다.

5 ≤ num_list의 길이 ≤ 50
-9 ≤ num_list의 원소 ≤ 9
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(num_list):
    sum_e = sum(num_list[::2])
    sum_o = sum(num_list[1::2])
    return sum_e if sum_e >= sum_o else sum_o


if __name__ == '__main__':
    solution([4, 2, 6, 1, 7, 6])
    solution([-1, 2, 5, 6, 3])

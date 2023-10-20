"""
리스트 자르기

정수 n과 정수 3개가 담긴 리스트 slicer 그리고 정수 여러 개가 담긴 리스트 num_list가 주어집니다.
slicer에 담긴 정수를 차례대로 a, b, c라고 할 때, n에 따라 다음과 같이 num_list를 슬라이싱 하려고 합니다.

n = 1 : num_list의 0번 인덱스부터 b번 인덱스까지
n = 2 : num_list의 a번 인덱스부터 마지막 인덱스까지
n = 3 : num_list의 a번 인덱스부터 b번 인덱스까지
n = 4 : num_list의 a번 인덱스부터 b번 인덱스까지 c 간격으로

올바르게 슬라이싱한 리스트를 return하도록 solution 함수를 완성해주세요.

n 은 1, 2, 3, 4 중 하나입니다.
slicer의 길이 = 3
slicer에 담긴 정수를 차례대로 a, b, c라고 할 때

0 ≤ a ≤ b ≤ num_list의 길이 - 1
1 ≤ c ≤ 3
5 ≤ num_list의 길이 ≤ 30
0 ≤ num_list의 원소 ≤ 100

3	[1, 5, 2]	[1, 2, 3, 4, 5, 6, 7, 8, 9]	[2, 3, 4, 5, 6]
4	[1, 5, 2]	[1, 2, 3, 4, 5, 6, 7, 8, 9]	[2, 4, 6]
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(n, slicer, num_list):
    A, B, C, LAST_INDEX = 0, 1, 2, len(num_list)
    if n == 1:
        S, E, STEP = 0, slicer[B], 1
    elif n == 2:
        S, E, STEP = slicer[A], LAST_INDEX, 1
    elif n == 3:
        S, E, STEP = slicer[A], slicer[B],1
    elif n == 4:
        S, E, STEP = slicer[A], slicer[B], slicer[C]
    else:
        raise Exception

    return num_list[S:E+1:STEP]


if __name__ == '__main__':
    assert solution(1, [1, 5, 2], [1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 2, 3, 4, 5, 6]
    assert solution(3, [1, 5, 2], [1, 2, 3, 4, 5, 6, 7, 8, 9]) == [2, 3, 4, 5, 6]
    assert solution(4, [1, 5, 2], [1, 2, 3, 4, 5, 6, 7, 8, 9]) == [2, 4, 6]

    # 알아야 할 것
    # 쿼리(n) 종류가 많아지면 2분할 방식으로 2이하, 3이상 으로 만들어주면(2진트리)
    # n:1~4까지 어떤 경우든 조건문 2번 안에 자리를 찾아 들어가게 됩니다!

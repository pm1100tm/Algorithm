"""
수열과 구간 쿼리 4

정수 배열 arr와 2차원 정수 배열 queries이 주어집니다.
queries의 원소는 각각 하나의 query를 나타내며, [s, e, k] 꼴입니다.
각 query마다 순서대로 s ≤ i ≤ e인 모든 i에 대해 i가 k의 배수이면 arr[i]에 1을 더합니다.
위 규칙에 따라 queries를 처리한 이후의 arr를 return 하는 solution 함수를 완성해 주세요.

1 ≤ arr의 길이 ≤ 1,000
0 ≤ arr의 원소 ≤ 1,000,000
1 ≤ queries의 길이 ≤ 1,000
0 ≤ s ≤ e < arr의 길이
0 ≤ k ≤ 5

[0, 1, 2, 4, 3]	[[0, 4, 1],[0, 3, 2],[0, 3, 3]]	[3, 2, 4, 6, 4]
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(arr, queries):
    for s, e, k in queries:
        if not k:
            break

        for index, n in enumerate(arr[s:e + 1]):
            if (index + s) % k == 0:
                arr[index+s] += 1

    return arr


if __name__ == '__main__':
    assert solution([0, 1, 2, 4, 3], [[0, 4, 1], [0, 3, 2], [0, 3, 3]]) == [3, 2, 4, 6, 4]
    solution([0, 1, 2, 4, 3], [[0, 4, 0], [0, 3, 2], [0, 3, 3]])

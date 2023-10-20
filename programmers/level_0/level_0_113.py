"""
수열과 구간 쿼리 1

두 정수 a, d와 길이가 n인 boolean 배열 included가 주어집니다.
첫째항이 a, 공차가 d인 등차수열에서 included[i]가 i + 1항을 의미할 때,
이 등차수열의 1항부터 n항까지 included가 true인 항들만 더한 값을 return 하는 solution 함수를 작성해 주세요.

1 ≤ arr의 길이 ≤ 1,000
0 ≤ arr의 원소 ≤ 1,000,000
1 ≤ queries의 길이 ≤ 1,000
0 ≤ s ≤ e < arr의 길이

[0, 1, 2, 3, 4]	[[0, 1],[1, 2],[2, 3]]	[1, 3, 4, 4, 4]
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(arr, queries):
    for q in queries:
        s, e = q
        for i in range(s, e+1):
            arr[i] += 1

    return arr


@prvalue(print_result=True)
def solution001(arr, queries):
    for q in queries:
        arr[q[0] : q[-1] + 1] += 1

    return arr


if __name__ == '__main__':
    assert solution([0, 1, 2, 3, 4], [[0, 1],[1, 2],[2, 3]])
    assert solution001([0, 1, 2, 3, 4], [[0, 1],[1, 2],[2, 3]])

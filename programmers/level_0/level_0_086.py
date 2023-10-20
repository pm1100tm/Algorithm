"""
특별한 이차원 배열 2

n × n 크기의 이차원 배열 arr이 매개변수로 주어질 때,
arr이 다음을 만족하면 1을 아니라면 0을 return 하는 solution 함수를 작성해 주세요.
0 ≤ i, j < n인 정수 i, j에 대하여 arr[i][j] = arr[j][i]

1 ≤ arr의 길이 = arr의 원소의 길이 ≤ 100
1 ≤ arr의 원소의 원소 ≤ 1,000
모든 arr의 원소의 길이는 같습니다.
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(arr: list[list[int]]) -> int:
    n_list = [n for n in range(len(arr))]
    for i, int_list in enumerate(arr):
        for j in n_list:
            if arr[i][j] != arr[j][i]:
                return 0

    return 1


@prvalue(print_result=True)
def solution001(arr: list[list[int]]) -> int:
    return int(arr == list(map(list, zip(*arr))))


if __name__ == '__main__':
    assert solution([[5, 192, 33], [192, 72, 95], [33, 95, 999]]) == 1
    assert solution(
        [
            [19, 498, 258, 587]
            , [63, 93, 7, 754]
            , [258, 7, 1000, 723]
            , [587, 754, 723, 81]
        ]
    ) == 0

    assert solution001(
        [
            [5, 192, 33]
            ,[192, 72, 95]
            ,[33, 95, 999]
        ]
    ) == 1
    assert solution001(
        [
            [19, 498, 258, 587]
            ,[63, 93, 7, 754]
            ,[258, 7, 1000, 723]
            ,[587, 754, 723, 81]
        ]
    ) == 0

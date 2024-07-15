"""연속 부분 수열 합의 개수
https://school.programmers.co.kr/learn/courses/30/lessons/131701
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(elements: list[int]) -> int:
    n = len(elements)
    extended_elements = elements * 2
    unique_sums = set()

    for i in range(1, n + 1):
        current_sum = sum(extended_elements[:i])
        unique_sums.add(current_sum)

        for j in range(1, n):
            current_sum += (
                extended_elements[j + i - 1] -
                extended_elements[j - 1]
            )
            unique_sums.add(current_sum)

    return len(unique_sums)


if __name__ == '__main__':
    assert solution([7, 9, 1, 1, 4]) == 18

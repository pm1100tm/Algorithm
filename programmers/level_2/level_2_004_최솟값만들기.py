"""최솟값 만들기
https://school.programmers.co.kr/learn/courses/30/lessons/12941
"""
from collections import deque
from utils import prvalue


@prvalue(print_result=True)
def solution(a: list[int], b: list[int]):
    """
    실패 및 시간초과
    """
    que_b = deque(b)
    min_v = None
    n = len(a)
    while n > 0:
        total = sum([a[i] * que_b[i] for i in range(len(a))])
        if min_v is None:
            min_v = total
        else:
            min_v = min(min_v, total)

        que_b.rotate()
        n -= 1

    return min_v


@prvalue(print_result=True)
def solution2(a: list[int], b: list[int]):
    """
    하나의 배열은 오름차순으로, 나머지 하나의 배열은 내림차순으로 정렬 후, 각각의 값을 곱한 값이 최솟값
    """
    a.sort()
    b.sort(reverse=True)
    answer = 0
    for i in range(len(a)):
        answer += a[i] * b[i]

    return answer


if __name__ == '__main__':
    assert solution2([1, 4, 2], [5, 4, 4]) == 29
    assert solution2([1, 2], [3, 4]) == 10

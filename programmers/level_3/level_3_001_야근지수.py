"""야근 지수
https://school.programmers.co.kr/learn/courses/30/lessons/12927
"""
import heapq

from utils import prvalue


@prvalue(print_result=True)
def solution(n: int, works: list[int]) -> int:
    max_heap = []
    heapq.heapify(max_heap)
    for w in works:
        heapq.heappush(max_heap, -w)

    for _ in range(n):
        v = -heapq.heappop(max_heap) - 1
        heapq.heappush(max_heap, 0 if v < 0 else -v)

    return sum([int(x)**2 for x in max_heap])


if __name__ == '__main__':
    assert solution(4, [4, 3, 3]) == 12
    assert solution(1, [2, 1, 2]) == 6
    assert solution(3, [1, 1]) == 0

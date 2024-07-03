"""프로세스
https://school.programmers.co.kr/tryouts/85932/challenges?language=python3
"""
import heapq

from collections import deque
from utils import prvalue


@prvalue(print_result=True)
def solution(priorities: list[int], location: int) -> int:
    queue = deque([(priority, i) for i, priority in enumerate(priorities)])
    max_heap = [-p for p in priorities]
    heapq.heapify(max_heap)
    execution_count = 0
    answer = 0

    while queue:
        p, i = queue.popleft()
        if p != -max_heap[0]:
            queue.append((p, i))
        else:
            execution_count += 1
            heapq.heappop(max_heap)
            if i == location:
                answer = execution_count
                break

    return answer


if __name__ == '__main__':
    assert solution([2, 1, 3, 2], 2) == 1
    assert solution([1, 1, 9, 1, 1, 1], 0) == 5

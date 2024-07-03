"""더 맵게
https://school.programmers.co.kr/tryouts/85934/challenges?language=python3
"""
import heapq

from utils import prvalue


@prvalue(print_result=True)
def solution(scoville: list[int], k: int) -> int:
    """
    섞은 음식의 스코빌 지수
     = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
    """
    min_heap = []
    heapq.heapify(min_heap)
    for s in scoville:
        heapq.heappush(min_heap, s)

    answer = 0
    while True:
        fir_min = heapq.heappop(min_heap)
        if fir_min >= k:
            break

        if not len(min_heap):
            answer = -1
            break

        sec_min = heapq.heappop(min_heap)
        heapq.heappush(min_heap, fir_min + (sec_min * 2))
        answer += 1

    return answer


if __name__ == '__main__':
    assert solution([1, 2, 3, 9, 10, 12], 7) == 2
    assert solution([2, 1], 7) == -1

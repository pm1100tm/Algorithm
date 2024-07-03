"""명예의전당(1)
https://school.programmers.co.kr/learn/courses/30/lessons/138477
"""
import heapq


def solution(k: int, score: list[int]) -> list[int]:
    answer = []
    rank = []
    for s in score:
        rank.append(s)
        rank.sort(reverse=True)
        if len(rank) <= k:
            answer.append(rank[-1])
        else:
            rank.pop()
            answer.append(rank[-1])

    return answer


def solution2(k: int, score: list[int]) -> list[int]:
    answer = []
    min_heap = []

    for s in score:
        if len(min_heap) < k:
            heapq.heappush(min_heap, s)
        else:
            if s > min_heap[0]:
                heapq.heappushpop(min_heap, s)

        answer.append(min_heap[0])

    return answer


if __name__ == '__main__':
    assert (
        solution(3, [10, 100, 20, 150, 1, 100, 200])
    ) == [10, 10, 10, 20, 20, 100, 100]
    assert (
        solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000])
    ) == [0, 0, 0, 0, 20, 40, 70, 70, 150, 300]
    assert (
        solution2(3, [10, 100, 20, 150, 1, 100, 200])
    ) == [10, 10, 10, 20, 20, 100, 100]
    assert (
        solution2(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000])
    ) == [0, 0, 0, 0, 20, 40, 70, 70, 150, 300]

"""명예의 전당
https://school.programmers.co.kr/tryouts/85933/challenges?language=python3
"""
import heapq

from utils import prvalue


@prvalue(print_result=True)
def solution(k: int, score: list[int]):
    que = []
    heapq.heapify(que)
    answer = []
    for i, s in enumerate(score, 1):
        if i <= k:
            heapq.heappush(que, s)
        else:
            if s > que[0]:
                heapq.heappushpop(que, s)

        answer.append(que[0])

    return answer


if __name__ == '__main__':
    assert (
        solution(3, [10, 100, 20, 150, 1, 100, 200])
    ) == [10, 10, 10, 20, 20, 100, 100]
    assert (
       solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000])
   ) == [0, 0, 0, 0, 20, 40, 70, 70, 150, 300]

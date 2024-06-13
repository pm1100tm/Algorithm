"""명예의전당(1)
매일 1명의 가수가 노래를 부르고, 시청자들의 문자 투표수로 가수에게 점수를 부여합니다. 매일 출연한 가수의
점수가 지금까지 출연 가수들의 점수 중 상위 k번째 이내이면 해당 가수의 점수를 명예의 전당이라는 목록에 올려
기념합니다. 즉 프로그램 시작 이후 초기에 k일까지는 모든 출연 가수의 점수가 명예의 전당에 오르게 됩니다.
k일 다음부터는 출연 가수의 점수가 기존의 명예의 전당 목록의 k번째 순위의 가수 점수보다 더 높으면,
출연 가수의 점수가 명예의 전당에 오르게 되고 기존의 k번째 순위의 점수는 명예의 전당에서 내려오게 됩니다.
명예의 전당 목록의 점수의 개수 k, 1일부터 마지막 날까지 출연한 가수들의 점수인 score가 주어졌을 때,
매일 발표된 명예의 전당의 최하위 점수를 return하는 solution 함수를 완성해주세요.

입출력 예
- 3	[10, 100, 20, 150, 1, 100, 200]
  [10, 10, 10, 20, 20, 100, 100]
- 4	[0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]
  [0, 0, 0, 0, 20, 40, 70, 70, 150, 300]
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
        == [10, 10, 10, 20, 20, 100, 100]
    )
    assert (
        solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000])
        == [0, 0, 0, 0, 20, 40, 70, 70, 150, 300]
    )
    assert (
        solution2(3, [10, 100, 20, 150, 1, 100, 200])
        == [10, 10, 10, 20, 20, 100, 100]
    )
    assert (
        solution2(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000])
        == [0, 0, 0, 0, 20, 40, 70, 70, 150, 300]
    )

    sample_heap()

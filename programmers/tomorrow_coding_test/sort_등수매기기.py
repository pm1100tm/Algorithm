"""등수 매기기
https://school.programmers.co.kr/tryouts/85944/challenges?language=python3
"""
import pytest
import statistics
from utils import prvalue


@prvalue(print_result=True)
def solution(score: list[list[int]]) -> list[int]:
    avgs = [(statistics.mean(s), i) for i, s in enumerate(score)]
    sorted_avgs = sorted(avgs, key=lambda x: x[0], reverse=True)
    answer = [0] * len(score)

    cur_rank = 1
    prev_avg = None
    same_cnt = 0
    for (avg, origin_index) in sorted_avgs:
        if avg != prev_avg:
            answer[origin_index] = cur_rank
            cur_rank += 1
            same_cnt = 0
        else:
            same_cnt += 1
            answer[origin_index] = cur_rank - same_cnt
            cur_rank += 1

        prev_avg = avg

    return answer


@prvalue(print_result=True)
def solution2(score: list[list[int]]) -> list[int]:
    """
    평균 값으로 내림차순 하는 것은, 합계를 내림차순 하는 것과 같은 결과이다.
    index 메서드는 가장 앞의 인덱스 값을 리턴한다.
    """
    sum_list = sorted([sum(s) for s in score], reverse=True)
    return [sum_list.index(sum(s)) + 1 for s in score]


@pytest.mark.parametrize(
    'score, expected',
    [
        (
            [[80, 70], [90, 50], [40, 70], [50, 80]],
            [1, 2, 4, 3],
        ),
        (
            [[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]],
            [4, 4, 6, 2, 2, 1, 7]
        ),
    ]
)
def test_solution(score, expected):
    assert solution(score) == expected, 'failed'
    assert solution2(score) == expected, 'failed'

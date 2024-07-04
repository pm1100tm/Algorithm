"""실패율
https://school.programmers.co.kr/tryouts/85943/challenges?language=python3
"""
import pytest
from collections import Counter
from utils import prvalue


@prvalue(print_result=True)
def solution(n: int, stages: list[int]) -> list[int]:
    num = len(stages)
    counter = Counter(stages)

    failure_per = []
    for stage_num in range(1, n + 1):
        challenging_num = counter.get(stage_num, 0)
        try:
            per = (challenging_num / num) * 100
        except ZeroDivisionError:
            per = 0

        failure_per.append((stage_num, per))
        num -= challenging_num

    answer = [
        stage_num for stage_num, _ in
        sorted(failure_per, key=lambda x: (x[1], -x[0]), reverse=True)
    ]

    return answer


@pytest.mark.parametrize(
    'n, stages, expected',
    [
        (5, [2, 1, 2, 6, 2, 4, 3, 3], [3,4,2,1,5]),
        (4, [4,4,4,4,4]	, [4,1,2,3]),
        (4, [1,1,1,1,1]	, [1,2,3,4]),
    ]
)
def test_solution(n, stages, expected):
    assert solution(n, stages) == expected, 'failed'

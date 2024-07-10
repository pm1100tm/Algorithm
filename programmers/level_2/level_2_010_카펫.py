"""카펫
https://school.programmers.co.kr/learn/courses/30/lessons/42842
"""
import math

from utils import prvalue


@prvalue(print_result=True)
def solution(brown: int, yellow: int) -> list[int]:
    answer = []
    total = brown + yellow
    sqrt_n = int(math.sqrt(total))
    for i in range(sqrt_n + 1, 2, -1):
        if total % i == 0:
            w = max(i, total // i)
            h = min(i, total // i)
            if (w - 2) * (h - 2) == yellow:
                answer += [w] + [h]
                break

    return answer


if __name__ == '__main__':
    assert solution(10, 2) == [4, 3]
    assert solution(8, 1) == [3, 3]
    assert solution(24, 24) == [8, 6]

"""연속된 수의 합
https://school.programmers.co.kr/tryouts/85899/challenges?language=python3
"""
from utils import prvalue


@prvalue(print_result=False)
def solution(num, total):
    start = int((total / num) - ((num - 1) / 2))
    return [v for v in range(start, start + num)]


def solution2(num: int, total: int):
    answer = []
    n = total // num
    while True:
        for i in range(n, n + num):
            answer.append(i)

        if sum(answer) == total:
            break
        else:
            n -= 1
            answer.clear()

    return answer


if __name__ == '__main__':
    assert solution(1, 0) == [0]
    assert solution(1, 12) == [12]
    assert solution(3, 12) == [3, 4, 5]
    assert solution(5, 15) == [1, 2, 3, 4, 5]
    assert solution(4, 14) == [2, 3, 4, 5]
    assert solution(5, 5) == [-1, 0, 1, 2, 3]

    assert solution2(1, 0) == [0]
    assert solution2(1, 12) == [12]
    assert solution2(3, 12) == [3, 4, 5]
    assert solution2(5, 15) == [1, 2, 3, 4, 5]
    assert solution2(4, 14) == [2, 3, 4, 5]
    assert solution2(5, 5) == [-1, 0, 1, 2, 3]

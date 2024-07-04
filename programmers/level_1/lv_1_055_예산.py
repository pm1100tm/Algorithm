""" 예산
https://school.programmers.co.kr/learn/courses/30/lessons/12982
"""


def solution(d: list[int], budget: int) -> int:
    d.sort()
    count, total = 0, budget
    for v in d:
        total -= v
        if total >= 0:
            count += 1

    return count


def solution2(d: list[int], budget: int) -> int:
    d.sort()
    total = sum(d)
    if total <= budget:
        return len(d)

    d.pop()

    return solution2(d, budget)


if __name__ == '__main__':
    assert solution([1, 3, 2, 5, 4], 9) == 3
    assert solution([2, 2, 3, 3], 10) == 4

    assert solution2([1, 3, 2, 5, 4], 9) == 3
    assert solution2([2, 2, 3, 3], 10) == 4

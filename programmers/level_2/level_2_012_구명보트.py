"""구명보트
https://school.programmers.co.kr/learn/courses/30/lessons/42885
- idea
Greedy(탐욕법)
"""
from utils import prvalue
from collections import deque


@prvalue(print_result=True)
def solution(people: list[int], limit: int) -> int:
    people.sort()
    l_index, r_index = 0, len(people) - 1
    boats = 0

    while l_index <= r_index:
        if people[l_index] + people[r_index] <= limit:
            l_index += 1
        r_index -= 1
        boats += 1

    return boats


def solution2(people: list[int], limit: int) -> int:
    que = deque(sorted(people))
    cnt = 0
    while que:
        l = que.popleft()
        if not que:
            cnt += 1
            break

        r = que.pop()
        if l + r > limit:
            que.appendleft(l)

        cnt += 1

    return cnt


if __name__ == '__main__':
    assert solution([70, 50, 80, 50], 100) == 3
    assert solution([70, 80, 50], 100) == 3
    assert solution([70, 80], 100) == 2
    assert solution([50, 50], 100) == 1
    assert solution([50, 70], 100) == 2
    assert solution([20, 20, 20, 30, 70], 100) == 3
    assert solution([2, 3, 4, 5, 5, 8], 10) == 3
    assert solution([2, 3, 4, 5, 5, 10], 10) == 4

    assert solution2([70, 50, 80, 50], 100) == 3
    assert solution2([70, 80, 50], 100) == 3
    assert solution2([70, 80], 100) == 2
    assert solution2([50, 50], 100) == 1
    assert solution2([50, 70], 100) == 2
    assert solution2([20, 20, 20, 30, 70], 100) == 3
    assert solution2([2, 3, 4, 5, 5, 8], 10) == 3
    assert solution2([2, 3, 4, 5, 5, 10], 10) == 4

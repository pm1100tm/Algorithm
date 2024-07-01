"""카드뭉치
https://school.programmers.co.kr/tryouts/85903/challenges?language=python3
"""
from collections import deque


def solution(cards1, cards2, goal):
    """two pointer
    """
    p1, p2, pg = 0, 0, 0
    p1_len, p2_len = len(cards1), len(cards2)
    answer = True
    while pg < len(goal):
        target = goal[pg]
        if p1 < p1_len and cards1[p1] == target:
            p1 += 1
        elif p2 < p2_len and cards2[p2] == target:
            p2 += 1
        else:
            answer = False
            break
        pg += 1

    return 'Yes' if answer else 'No'


def solution2(cards1: list[str], cards2: list[str], goal: list[str]):
    """deque
    """
    c1 = deque(cards1)
    c2 = deque(cards2)
    answer = True
    for g in goal:
        if c1 and c1[0] == g:
            c1.popleft()
        elif c2 and c2[0] == g:
            c2.popleft()
        else:
            answer = False
            break

    return 'Yes' if answer else 'No'


if __name__ == '__main__':
    assert solution(
        ["i", "drink", "water"],
        ["want", "to"],
        ["i", "want", "to", "drink", "water"],
    ) == 'Yes'
    assert solution(
        ["i", "water", "drink"],
        ["want", "to"],
        ["i", "want", "to", "drink", "water"]
    ) == 'No'

    assert solution2(
        ["i", "drink", "water"],
        ["want", "to"],
        ["i", "want", "to", "drink", "water"],
    ) == 'Yes'
    assert solution2(
        ["i", "water", "drink"],
        ["want", "to"],
        ["i", "want", "to", "drink", "water"]
    ) == 'No'

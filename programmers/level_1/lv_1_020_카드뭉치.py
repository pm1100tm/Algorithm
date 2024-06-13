"""추억점수
"""
from collections import deque


def solution(card1: list[str], card2: list[str], goal: list[str]):
    answer = 'Yes'
    c1, c2 = deque(card1), deque(card2)

    for word in goal:
        if c1 and c1[0] == word:
            c1.popleft()
        elif c2 and c2[0] == word:
            c2.popleft()
        else:
            answer = 'No'
            break
    print(answer)
    return answer


if __name__ == '__main__':
    solution(
        ["i", "drink", "water"],
        ["want", "to"],
        ["i", "want", "to", "drink", "water"],
    )
    solution(
        ["i", "drink", "water"],
        ["want", "to"],
        ["i", "want", "to", "to", "drink", "water"],
    )

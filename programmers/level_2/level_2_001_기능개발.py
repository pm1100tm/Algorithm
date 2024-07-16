"""기능 개발
https://school.programmers.co.kr/learn/courses/30/lessons/42586
"""
from utils import prvalue

from collections import deque


@prvalue(print_result=False)
def solution(progresses: list[int], speeds: list[int]) -> list[int]:
    que1 = deque(progresses)
    que2 = deque(speeds)
    answer = []
    while que1:
        for i in range(len(que1)):
            que1[i] += que2[i]

        count = 0
        while que1:
            if que1[0] >= 100:
                que1.popleft()
                que2.popleft()
                count += 1
            else:
                break

        if count:
            answer.append(count)

    return answer


if __name__ == '__main__':
    assert solution([93, 30, 55], [1, 30, 5]) == [2, 1]
    assert solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]) == [1, 3, 2]

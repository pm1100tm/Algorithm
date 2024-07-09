"""짝지어 제거하기
https://school.programmers.co.kr/learn/courses/30/lessons/12973
"""
from collections import deque
from utils import prvalue


@prvalue(print_result=True)
def solution(s: str) -> int:
    answer = 0
    que = deque(s)
    for _ in range(len(s)):
        if len(que) < 2:
            break
        if que.popleft() == que[0]:
            que.popleft()

        if not que:
            answer = 1
            break

    return answer


@prvalue(print_result=True)
def solution(s: str) -> int:
    stack = []
    for i, char in enumerate(s):
        if not stack:
            stack.append(char)
            continue

        if stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])

    return 1 if not stack else 0


if __name__ == '__main__':
    assert solution('baabaa') == 1
    assert solution('cdcd') == 0
    assert solution('aaaaaaaaaaaaa') == 0

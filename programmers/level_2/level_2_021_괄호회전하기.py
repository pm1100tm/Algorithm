"""괄호 회전하기
https://school.programmers.co.kr/learn/courses/30/lessons/76502
- Idea
Stack, Queue
"""
from utils import prvalue

from collections import deque


@prvalue(print_result=True)
def solution(s: str) -> int:

    def is_valid_parentheses(_s: str) -> bool:
        dic = {')': '(', '}': '{', ']': '['}
        stack = []
        for char in _s:
            if char in '({[':
                stack.append(char)
                continue
            if not stack:
                return False
            if dic[char] != stack.pop():
                return False

        return False if stack else True

    x = 0
    que = deque(s)
    for _ in range(0, len(s)):
        if is_valid_parentheses(''.join(que)):
            x += 1
        que.rotate(-1)

    return x


if __name__ == '__main__':
    assert solution('[]()') == 2
    assert solution(')(') == 1
    assert solution(')([') == 0
    assert solution('{(})') == 0
    assert solution('[](){}') == 3
    assert solution("}]()[{") == 2
    assert solution("[)(]") == 0
    assert solution("}}}") == 0

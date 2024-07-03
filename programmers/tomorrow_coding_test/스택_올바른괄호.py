"""올바른 괄호
https://school.programmers.co.kr/tryouts/85929/challenges?language=python3
"""


def solution(s: str) -> bool:
    if s[0] == ')':
        return False

    stack = []
    for v in s:
        if v == '(':
            stack.append(v)
        else:
            if stack: # IndexError if excute pop for empty list
                stack.pop()

    return True if not stack else False


if __name__ == '__main__':
    assert solution("()()") is True
    assert solution("(())()") is True
    assert solution(")()(") is False
    assert solution("(()(") is False

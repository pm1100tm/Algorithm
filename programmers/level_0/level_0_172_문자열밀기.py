"""문자열밀기
문자열을 A를 밀어서 B와 같아 질 때의 횟수를 리턴하라.
같아질 수 없다면 -1을 리턴하라.
"""
from collections import deque


def solution(A: str, B: str) -> int:
    """문자열 밀기
    deque를 활용하여 문자열을 밀 수 있다.
    """
    count = 0
    deq = deque(A)

    for _ in range(len(A)):
        if ''.join(deq) == B:
            break
        deq.rotate()
        count += 1

    if count == len(A):
        count = -1

    return count


if __name__ == '__main__':
    assert solution('hello', 'ohell') == 1
    assert solution('apple', 'elppa') == -1
    assert solution('atat', 'tata') == 1
    assert solution('abc', 'abc') == 0
    assert solution('abce', 'abcd') == -1

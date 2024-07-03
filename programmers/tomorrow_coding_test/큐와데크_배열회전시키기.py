"""배열 회전시키기
https://school.programmers.co.kr/tryouts/85930/challenges?language=python3
"""
from utils import prvalue
from collections import deque


@prvalue(print_result=True)
def solution(numbers: list[int], direction: str):
    que = deque(numbers)
    num = -1 if direction == 'left' else 1
    que.rotate(num)

    return list(que)


if __name__ == '__main__':
    assert solution([1, 2, 3], "right") == [3, 1, 2]
    assert solution([4, 455, 6, 4, -1, 45, 6], "left") == [455, 6, 4, -1, 45, 6, 4]


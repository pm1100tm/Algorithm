"""
배열 회전시키기

정수가 담긴 배열 numbers와 문자열 direction가 매개변수로 주어집니다.
배열 numbers의 원소를 direction방향으로 한 칸씩 회전시킨 배열을 return하도록 solution 함수를 완성해주세요.

3 ≤ numbers의 길이 ≤ 20
direction은 "left" 와 "right" 둘 중 하나입니다.

[1, 2, 3]	"right"	[3, 1, 2]
[4, 455, 6, 4, -1, 45, 6]	"left"	[455, 6, 4, -1, 45, 6, 4]
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(numbers: list[int], direction: str):
    if direction == "right":
        number = numbers.pop()
        return [number] + numbers

    else:
        _numbers = numbers[::-1]
        number = _numbers.pop()
        answer = [number] + _numbers
        return answer[::-1]


@prvalue(print_result=True)
def solution001(numbers: list[int], direction: str):
    if direction == "right":
        return numbers[-1:] + numbers[:-1]
    else:
        return numbers[1:] + numbers[:1]


@prvalue(print_result=True)
def solution002(numbers: list[int], direction: str):
    from collections import deque

    _numbers = deque(numbers)
    if direction == "right":
        _numbers.rotate(1)
    else:
        _numbers.rotate(-1)

    return list(_numbers)


if __name__ == '__main__':
    assert solution([1, 2, 3], "right") == [3, 1, 2]
    assert solution([4, 455, 6, 4, -1, 45, 6], "left") == [455, 6, 4, -1, 45, 6, 4]
    assert solution001([1, 2, 3], "right") == [3, 1, 2]
    assert solution001([4, 455, 6, 4, -1, 45, 6], "left") == [455, 6, 4, -1, 45, 6, 4]
    assert solution002([1, 2, 3], "right") == [3, 1, 2]
    assert solution002([4, 455, 6, 4, -1, 45, 6], "left") == [455, 6, 4, -1, 45, 6, 4]

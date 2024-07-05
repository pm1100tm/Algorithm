"""이웃한 칸
https://school.programmers.co.kr/learn/courses/30/lessons/250125
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(board, h, w) -> int:
    count = 0
    color = board[h][w]
    max_i = len(board) - 1
    directions = [
        (0, 1), # right
        (0, -1), # left
        (-1, 0), # up
        (1, 0), # down
    ]

    for _h, _w in directions:
        check_h = 0 <= h + _h <= max_i
        check_w = 0 <= w + _w <= max_i
        if check_h and check_w:
            compare = board[h + _h][w + _w]
            if color == compare:
                count += 1

    return count


if __name__ == '__main__':
    assert solution(
        [
            ["blue", "red", "orange", "red"],
            ["red", "red", "blue", "orange"],
            ["blue", "orange", "red", "red"],
            ["orange", "orange", "red", "blue"],
        ],
        1,
        1,
    ) == 2
    assert solution(
        [
            ["yellow", "green", "blue"],
            ["blue", "green", "yellow"],
            ["yellow", "blue", "blue"]
        ],
        0,
        1,
    ) == 1

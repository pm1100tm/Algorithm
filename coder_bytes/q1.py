"""QueneCheck
https://github.com/gutty333/Hard-Programming-Challenges/blob/master/22_QueenCheck.cpp
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(str_arr: list[str]):
    move = [
        (0, -1),  # up
        (0, 1),  # down
        (-1, 0),  # left
        (1, 0),  # righ
        (-1, -1),  # left up
        (1, -1),  # right up
        (-1, 1),  # left down
        (1, 1),  # right down
    ]

    qx = int(str_arr[0][1])
    qy = int(str_arr[0][3])
    kx = int(str_arr[1][1])
    ky = int(str_arr[1][3])

    q_range = []
    k_range = []
    for (x, y) in move:
        # make king range
        move_kx, move_ky = kx + x, ky + y
        if 1 <= move_kx <= 8 and 1 <= move_ky <= 8:
            k_range.append([move_kx, move_ky])

        # make queen range
        move_qx, move_qy = qx, qy
        while True:
            move_qx += x
            move_qy += y
            if 1 <= move_qx <= 8 and 1 <= move_qy <= 8:
                q_range.append([move_qx, move_qy])
            else:
                break

    # If the original king position not be in q range, return -1
    if [kx, ky] not in q_range:
        return -1

    count = 0
    for k in k_range:
        if k not in q_range:
            count += 1

    return count


if __name__ == '__main__':
    solution(['(4,4)', '(6,6)']) # 6
    solution(['(1,1)', '(1,4)']) # 3
    solution(['(2,2)', '(2,3)']) # 3
    solution(['(1,8)', '(2,7)']) # 3
    solution(['(1,1)', '(8,1)']) # 2
    solution(['(8,2)', '(7,1)']) # 2
    solution(['(3,1)', '(4,4)']) # -1

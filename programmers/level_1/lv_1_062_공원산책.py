"""공원 산책
https://school.programmers.co.kr/learn/courses/30/lessons/172928
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(park, routes):
    min_h, max_h = 0, len(park) - 1
    min_w, max_w = 0, len(park[0]) - 1
    point = []
    for h, p in enumerate(park):
        w = p.find('S')
        if w != -1:
            point.append(h)
            point.append(w)
            break

    for r in routes:
        h, w = point[0], point[1]
        direction, move = r.split(' ')
        m = int(move)

        if direction == 'N' and h - m >= min_h:
            if all([park[h - i][w] != 'X' for i in range(1, m + 1)]):
                point[0] -= m

        if direction == 'S' and h + m <= max_h:
            if all([park[h + i][w] != 'X' for i in range(1, m + 1)]):
                point[0] += m

        if direction == 'W' and w - m >= min_w:
            if all([park[h][w - i] != 'X' for i in range(1, m + 1)]):
                point[1] -= m

        if direction == 'E' and w + m <= max_w:
            if all([park[h][w + i] != 'X' for i in range(1, m + 1)]):
                point[1] += m

    return point


if __name__ == '__main__':
    assert solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"]) == [2, 1]
    assert solution(["SOO","OXX","OOO"], ["E 2","S 2","W 1"]) == [0, 1]
    assert solution(["OSO","OOO","OXO","OOO"], ["E 2","S 3","W 1"]) == [0, 0]
    assert solution(
        ["OOOOO", "OOOOO", "OOSOO", "OOOOO", "OOOOO"],
        [
            "E 3", "W 3", "S 3", "N 3",
            "E 2",
            "E 1", "W 4", "W 1", "S 2", "S 1", "N 4",
            "N 1"
        ]
    ) == [0, 0]

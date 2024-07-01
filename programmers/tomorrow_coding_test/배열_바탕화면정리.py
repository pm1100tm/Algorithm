"""바탕화면 정리
https://school.programmers.co.kr/tryouts/85911/challenges
"""


def solution(wallpaper: list[str]):
    f = '#'
    min_col_points = []
    min_row_points = []
    max_col_points = []
    max_row_points = []

    for i, w in enumerate(wallpaper):
        for j, char in enumerate(w):
            if char != f:
                continue
            min_col_points.append(i)
            min_row_points.append(j)
            max_col_points.append(i + 1)
            max_row_points.append(j + 1)

    return [
        min(min_col_points), min(min_row_points),
        max(max_col_points), max(max_row_points),
    ]


if __name__ == '__main__':
    assert solution([".#...", "..#..", "...#."]) == [0, 1, 3, 4]
    assert solution(
        [
            "..........",
            ".....#....",
            "......##..",
            "...##.....",
            "....#.....",
        ]
    ) == [1, 3, 5, 8]
    assert solution(
        [
            ".##...##.",
            "#..#.#..#",
            "#...#...#",
            ".#.....#.",
            "..#...#..",
            "...#.#...",
            "....#....",
        ]
    ) == [0, 0, 7, 9]
    assert solution(["..", "#."]) == [1, 0, 2, 1]

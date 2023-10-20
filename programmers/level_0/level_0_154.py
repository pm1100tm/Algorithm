"""
양의 정수 n이 매개변수로 주어집니다. n × n 배열에 1부터 n2 까지 정수를 인덱스 [0][0]부터 시계방향
나선형으로 배치한 이차원 배열을 return 하는 solution 함수를 작성해 주세요.

4	[[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
5	[[1, 2, 3, 4, 5], [16, 17, 18, 19, 6], [15, 24, 25, 20, 7], [14, 23, 22, 21, 8], [13, 12, 11, 10, 9]]
"""
from utils import prvalue


@prvalue(print_result=False)
def solution(n):
    """
    필요 알고리즘 방법
    - 시뮬레이션(simulation)
    이슈:
    - answer = [[0] * n] * n
    - 위와 같은 방식으로 초기화하면, 내부의 리스트들이 모두 동일한 객체를 참조하게 되어, 하나의 리스트를
      변경하면, 다른 리스트들도 동일하게 변경된다. 이로 인해 의도한 대로 배열이 채워지지 않는다.
    """
    answer = [[0] * n for _ in range(n)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # right, down, left, up
    current_direction = 0
    row, col = 0, 0
    current_value = 1

    for _ in range(n * n):
        answer[row][col] = current_value
        current_value += 1

        if current_direction % 2 == 0:
            next_row = row
            next_col = col + directions[current_direction][1]
        else:
            next_row = row + directions[current_direction][0]
            next_col = col

        if (0 <= next_row < n and 0 <= next_col < n) and answer[next_row][next_col] == 0:
            row, col = next_row, next_col
        else:
            current_direction = (current_direction + 1) % 4 # direction constant value
            row += directions[current_direction][0]
            col += directions[current_direction][1]

    return answer


def solution2(n: int) -> list[list[int]]:
    answer = [[0] * n for _ in range(n)]
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)] # left, down, right, up
    current_direction = 0
    row, col = 0, 0

    for v in range(1, n**2 + 1):
        answer[row][col] = v
        next_row = row + direction[current_direction][0]
        next_col = col + direction[current_direction][1]

        if next_row >= n or next_col >= n or answer[next_row][next_col] != 0:
            current_direction = (current_direction + 1) % 4

        row = row + direction[current_direction][0]
        col = col + direction[current_direction][1]

    return answer


if __name__ == '__main__':
    assert solution(4) == [
        [1, 2, 3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10, 9, 8, 7],
    ]
    assert solution(5) == [
        [1, 2, 3, 4, 5],
        [16, 17, 18, 19, 6],
        [15, 24, 25, 20, 7],
        [14, 23, 22, 21, 8],
        [13, 12, 11, 10, 9],
    ]

    assert solution2(4) == [
        [1, 2, 3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10, 9, 8, 7],
    ]
    assert solution2(5) == [
        [1, 2, 3, 4, 5]
        , [16, 17, 18, 19, 6]
        , [15, 24, 25, 20, 7]
        , [14, 23, 22, 21, 8]
        , [13, 12, 11, 10, 9]
    ]

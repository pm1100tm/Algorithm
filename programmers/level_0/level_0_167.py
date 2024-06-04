"""
다음 그림과 같이 지뢰가 있는 지역과 지뢰에 인접한 위, 아래, 좌, 우 대각선 칸을 모두 위험지역으로 분류합니다.
지뢰는 2차원 배열 board에 1로 표시되어 있고 board에는 지뢰가 매설 된 지역 1과, 지뢰가 없는 지역 0만
존재합니다. 지뢰가 매설된 지역의 지도 board가 매개변수로 주어질 때, 안전한 지역의 칸 수를 return하도록
solution 함수를 완성해주세요.

제한사항
- board는 n * n 배열입니다.
- 1 ≤ n ≤ 100
- 지뢰는 1로 표시되어 있습니다.
- board에는 지뢰가 있는 지역 1과 지뢰가 없는 지역 0만 존재합니다.
"""
from utils import prvalue


@prvalue(print_result=False)
def solution(board):
    n = len(board)
    danger = {
        f'{i}-{j}': ''
        for i, line in enumerate(board, 1)
        for j, value in enumerate(line, 1)
    }

    for i, line in enumerate(board, 1):
        for j, value in enumerate(line, 1):
            if value == 0:
                continue
            danger[f'{i}-{j}'] = '*'
            if danger[f'{i}-{j}'] == '':
                continue

            danger[f'{i}-{j}'] = '*'
            if i - 1 >= 0:
                danger[f'{i-1}-{j}'] = 'red'
                if j - 1 >= 0:
                    danger[f'{i-1}-{j-1}'] = 'red'
                if j + 1 <= n:
                    danger[f'{i-1}-{j+1}'] = 'red'

            if j - 1 >= 0:
                danger[f'{i}-{j-1}'] = 'red'
            if j + 1 <= n:
                danger[f'{i}-{j+1}'] = 'red'

            if i + 1 <= n:
                danger[f'{i+1}-{j}'] = 'red'
                if j - 1 >= 0:
                    danger[f'{i+1}-{j-1}'] = 'red'
                if j + 1 <= n:
                    danger[f'{i+1}-{j+1}'] = 'red'

    return len([v for v in danger.values() if not v])


def solution2(board):
    n = len(board)

    # 위험지역 표시 배열 초기화
    danger_zone = [[0] * n for _ in range(n)]

    # 8방향
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1),
    ]

    for i in range(n):
        for j in range(n):
            if board[i][j] != 1:
                continue

            # 현재 위치 위험지역으로 설정
            danger_zone[i][j] = 1

            # 8방향 조사 후 위험지역 설정
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < n:
                    danger_zone[ni][nj] = 1

    # 이차원 배열 flat 으로 1차원 배열로 만든 후 0 인 데이터를 가진 리스트의 길이 리턴
    return len([data for data in danger_zone for _data in data if not _data])


if __name__ == '__main__':
    case1 = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    case2 = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0],
    ]
    case3 = [
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
    ]

    assert solution(case1) == 16
    assert solution(case2) == 13
    assert solution(case3) == 0

    assert solution2(case1) == 16
    assert solution2(case2) == 13
    assert solution2(case3) == 0

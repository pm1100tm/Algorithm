"""
머쓱이는 RPG게임을 하고 있습니다. 게임에는 up, down, left, right 방향키가 있으며 각 키를 누르면
위, 아래, 왼쪽, 오른쪽으로 한 칸씩 이동합니다.
예를 들어 [0,0]에서
- up을 누른다면 캐릭터의 좌표는 [0, 1],
- down을 누른다면 [0, -1],
- left를 누른다면 [-1, 0],
- right를 누른다면 [1, 0]입니다.
머쓱이가 입력한 방향키의 배열 keyinput와 맵의 크기 board이 매개변수로 주어집니다.
캐릭터는 항상 [0,0]에서 시작할 때 키 입력이 모두 끝난 뒤에 캐릭터의 좌표 [x, y]를 return하도록
solution 함수를 완성해주세요.

[0, 0]은 board의 정 중앙에 위치합니다. 예를 들어 board의 가로 크기가 9라면 캐릭터는 왼쪽으로
최대 [-4, 0]까지 오른쪽으로 최대 [4, 0]까지 이동할 수 있습니다.

제한사항
- board은 [가로 크기, 세로 크기] 형태로 주어집니다.
- board의 가로 크기와 세로 크기는 홀수입니다.
- board의 크기를 벗어난 방향키 입력은 무시합니다.
- 0 ≤ keyinput의 길이 ≤ 50
- 1 ≤ board[0] ≤ 99
- 1 ≤ board[1] ≤ 99
- keyinput은 항상 up, down, left, right만 주어집니다.
"""
from utils import prvalue


@prvalue(print_result=False)
def solution(keyinput, board):
    x, y = board[0] // 2, board[1] // 2
    max_x, min_x, max_y, min_y = x, -x, y, -y
    current_point = [0, 0]

    def set_point(cmd):
        match cmd:
            case 'left':
                point = current_point[0] - 1
                if min_x <= point:
                    current_point[0] = point
            case 'right':
                point = current_point[0] + 1
                if max_x >= point:
                    current_point[0] = point
            case 'up':
                point = current_point[1] + 1
                if max_y >= point:
                    current_point[1] = point
            case 'down':
                point = current_point[1] - 1
                if min_y <= point:
                    current_point[1] = point

    for move in keyinput:
        set_point(move)

    return current_point


def solution2(keyinput, board):
    max_x, max_y = board[0] // 2, board[1] // 2
    current_point = [0, 0]
    move = {
        'left':(-1,0),
        'right':(1,0),
        'up':(0,1),
        'down':(0,-1)
    }

    for cmd in keyinput:
        move_x, move_y = move[cmd]
        if (
            abs(current_point[0] + move_x) > max_x
            or abs(current_point[1] + move_y) > max_y
        ):
            continue

        current_point[0] += move_x
        current_point[1] += move_y

    return current_point


if __name__ == '__main__':
    # assert solution(["left", "right", "up", "right", "right"], [11, 11]) == [2, 1]
    # assert solution(["down", "down", "down", "down", "down"], [7, 9]) ==[0, -4]
    assert solution2(["left", "right", "up", "right", "right"], [11, 11]) == [2, 1]
    assert solution2(["down", "down", "down", "down", "down"], [7, 9]) == [0, -4]

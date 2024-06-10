"""
점 네 개의 좌표를 담은 이차원 배열  dots가 다음과 같이 매개변수로 주어집니다.

[[x1, y1], [x2, y2], [x3, y3], [x4, y4]]
주어진 네 개의 점을 두 개씩 이었을 때, 두 직선이 평행이 되는 경우가 있으면 1을 없으면 0을 return 하도록
solution 함수를 완성해보세요.

제한사항
- dots의 길이 = 4
- dots의 원소는 [x, y] 형태이며 x, y는 정수입니다.
- 0 ≤ x, y ≤ 100
- 서로 다른 두개 이상의 점이 겹치는 경우는 없습니다.
- 두 직선이 겹치는 경우(일치하는 경우)에도 1을 return 해주세요.
- 임의의 두 점을 이은 직선이 x축 또는 y축과 평행한 경우는 주어지지 않습니다.

pytest programmers/level_0/level_0_170_평행.py
"""


def cal_inclanation(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    if x2 - x1 == 0:
        return float('inf')

    return (y2 - y1) / (x2 - x1)


def solution(dots: list[list[int]]):
    length = len(dots)
    number_list = [i for i in range(length)]
    groups = []

    for i in range(length):
        for j in range(1, length):
            groups.append([i, j] + list(set(number_list) - {i, j}))
        break

    for g in groups:
        index1, index2 = g[:2]
        index3, index4 = g[2:]

        x1, y1 = dots[index1]
        x2, y2 = dots[index2]
        x3, y3 = dots[index3]
        x4, y4 = dots[index4]

        inc1 = cal_inclanation((x1, y1), (x2, y2))
        inc2 = cal_inclanation((x3, y3), (x4, y4))
        if inc1 == inc2:
            return 1

    return 0


def solution2(dots):
    """
    조합할 수 있는 점1, 점2 그룹과, 점3, 점4를 구성한다.
    점1, 점2 의 각도와 점3, 점4의 각도가 일치한다면, 평행한다고 가정할 수 있다.
    """
    length = len(dots)
    number_list = [i for i in range(length)]
    for i in range(length):
        for j in range(1, length):
            p1, p2 = dots[i], dots[j]
            index1, index2 = list(set(number_list) - {i, j})
            p3, p4 = dots[index1], dots[index2]
            if cal_inclanation(p1, p2) == cal_inclanation(p3, p4):
                return 1
        break

    return 0


if __name__ == '__main__':
    case1 = [[1, 4], [9, 2], [3, 8], [11, 6]]
    case2 = [[3, 5], [4, 1], [2, 4], [5, 10]]
    case3 = [[1, 1], [2, 2], [3, 3], [4, 4]]

    assert solution(case1) == 1
    assert solution(case2) == 0
    assert solution(case3) == 1

    assert solution2(case1) == 1
    assert solution2(case2) == 0
    assert solution2(case3) == 1

"""
선분 3개가 평행하게 놓여 있습니다. 세 선분의 시작과 끝 좌표가
[[start, end], [start, end], [start, end]] 형태로 들어있는 2차원 배열 lines가 매개변수로
주어질 때, 두 개 이상의 선분이 겹치는 부분의 길이를 return 하도록 solution 함수를 완성해보세요.

pytest programmers/level_0/level_0_171_겹치는선분의길이.py
"""


def solution(lines):
    """
    1. 모든 위치를 포함하는 리스트 초기화
    2. 각 선분의 구간을 리스트에 표시
    3. 2개 이상의 선분이 겹치는 구간의 길이 계산
    """
    coverage = [0] * 201
    for s, e in lines:
        for i in range(s + 100, e + 100):
            coverage[i] += 1

    answer = sum(1 for x in coverage if x > 1)

    return answer


if __name__ == '__main__':
    case1 = [[0, 1], [2, 5], [3, 9]]
    case2 = [[-1, 1], [1, 3], [3, 9]]
    case3 = [[0, 5], [3, 9], [1, 10]]
    case4 = [[-9, 5], [-2, 4], [-1, 4]]
    case5 = [[0, 2], [-3, -1], [-2, 1]]

    assert solution(case1) == 2
    assert solution(case2) == 0
    assert solution(case3) == 8
    assert solution(case4) == 6
    assert solution(case5) == 2

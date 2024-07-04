"""각도기
각에서 0도 초과 90도 미만은 예각,
90도는 직각, 90도 초과 180도 미만은 둔각 180도는 평각으로 분류합니다.
각 angle이 매개변수로 주어질 때 예각일 때 1, 직각일 때 2, 둔각일 때 3, 평각일 때 4
를 return하도록 solution 함수를 완성해주세요.
"""
from enum import IntEnum, unique
from typing import Final


ANGLE_090: Final[int] = 90
ANGLE_180: Final[int] = 180


@unique
class AngleType(IntEnum):
    Y = 1
    G = 2
    D = 3
    P = 4


def solution(angle: int):
    if angle < ANGLE_090:
        return AngleType.Y
    elif angle == ANGLE_090:
        return AngleType.G
    elif angle < ANGLE_180:
        return AngleType.D
    elif angle >= ANGLE_180:
        return AngleType.P

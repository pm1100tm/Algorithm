"""
나이계산

머쓱이는 40살인 선생님이 몇 년도에 태어났는지 궁금해졌습니다.
나이 age가 주어질 때, 2022년을 기준 출생 연도를 return 하는 solution 함수를 완성해주세요.
"""
from typing import Final


BASE_YEAR: Final[int] = 2022

MIN_AGE: Final[int] = 0
MAX_AGE: Final[int] = 120


def solution(age: int) -> int:
    if age < MIN_AGE:
        raise ValueError("age less than min value")
    if age > MAX_AGE:
        raise ValueError("age more than max value")

    return (BASE_YEAR - age) + 1

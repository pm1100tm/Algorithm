"""할인 행사
https://school.programmers.co.kr/learn/courses/30/lessons/131127
- Idea
Collection Counter, Hash
"""
from utils import prvalue

from collections import Counter


@prvalue(print_result=True)
def solution(want: list[str], number: list[int], discount: list[str]) -> int:
    wt_map = {k: v for k, v in zip(want, number)}

    # all을 사용하기 보다는 원하는 개수에 못미칠 때 바로 리턴
    def can_buy_all_discount_product(dis_map: dict) -> bool:
        for k, v in wt_map.items():
            if dis_map.get(k, 0) < v:
                return False
        return True

    # 0부터 10일 간의 카운터 객체 생성
    dc_map = Counter(discount[0:10])
    # 첫 days 계산
    days = 0 if not can_buy_all_discount_product(dc_map) else 1
    left = 0

    while left < len(discount) - 10:
        # 첫째날의 할인 품목 -1, 11일째의 품목 +1
        # 조건 상 값이 마이너스가 되지 않으나, 버그의 소지는 있음
        dc_map[discount[left]] -= 1
        dc_map[discount[left + 10]] += 1
        if can_buy_all_discount_product(dc_map):
            days += 1
        left += 1

    return days


if __name__ == '__main__':
    assert solution(
        ["banana", "apple", "rice", "pork", "pot"],
        [3, 2, 2, 2, 1],
        [
            "chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana",
            "pork", "rice", "pot", "banana", "apple", "banana",
        ],
    ) == 3

    assert solution(
        ["apple"],
        [10],
        [
            "banana", "banana", "banana", "banana", "banana", "banana", "banana",
            "banana", "banana", "banana",
        ]
    ) == 0

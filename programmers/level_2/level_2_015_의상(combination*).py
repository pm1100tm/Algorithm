"""의상
https://school.programmers.co.kr/learn/courses/30/lessons/42578
- idea
combinations(조합)
"""
from utils import prvalue

from collections import defaultdict
from itertools import product, combinations


@prvalue(print_result=True)
def solution(clothes: list[list[str]]) -> int:
    """
    시간초과: 케이스 1, 4, 7, 26
    """
    clothes_dict = defaultdict(list)
    for name, type_ in clothes:
        clothes_dict[type_].append(name)

    all_clothes = [clothes_dict[k] for k in clothes_dict.keys()]
    ret = []
    for i in range(1, len(all_clothes) + 1):
        for comb in combinations(all_clothes, i):
            for item in product(*comb):
                ret.append(item)

    return len(ret)


@prvalue(print_result=True)
def solution2(clothes: list[list[str]]) -> int:
    """
    시간초과: 케이스 1
    """
    clothes_dict = defaultdict(list)
    for name, type_ in clothes:
        clothes_dict[type_].append(name)

    all_clothes = [clothes_dict[k] for k in clothes_dict.keys()]
    count = 0
    for i in range(1, len(all_clothes) + 1):
        for comb in combinations(all_clothes, i):
            for _ in product(*comb):
                count += 1

    return count


@prvalue(print_result=True)
def solution3(clothes: list[list[str]]) -> int:
    clothes_dict = defaultdict(list)
    for name, type_ in clothes:
        clothes_dict[type_].append(name)

    n = 1
    for type_ in clothes_dict.keys():
        # 각 종류에서 선택할 수 있는 경우의 수는 해당 종류의 의상 수 + 1 이다.
        # 여기서 +1 은 해당 종류의 의상을 선택하지 않는 경우의 수를 포함한다
        # 예를 들어, headgear는 2개의 의상이 있으므로 선택할 수 있는 경우의 수는 2 + 1 = 3
        # 즉, ("yellow_hat", "green_turban", 선택하지 않음)
        n *= len(clothes_dict[type_]) + 1

    # 적어도 한 가지 이상의 옷을 입어야 하므로 옷을 전혀 선택하지 않는 시나리오를 고려하여 n - 1 처리
    return n - 1


if __name__ == '__main__':
    solution(
        [
            ["yellow_hat", "headgear"],
            ["blue_sunglasses", "eyewear"],
            ["green_turban", "headgear"],
        ]
    )
    solution(
        [
            ["crow_mask", "face"],
            ["blue_sunglasses", "face"],
            ["smoky_makeup", "face"],
        ]
    )

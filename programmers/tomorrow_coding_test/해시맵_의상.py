"""의상
https://school.programmers.co.kr/tryouts/85918/challenges?language=python3
"""
import itertools
from collections import defaultdict


def solution(clothes: list[list[str]]) -> int:
    """
    Failed
    """
    clothes_map = defaultdict(list)
    for name, type_ in clothes:
        clothes_map[type_].append(name)

    answer = 0
    data_list = [v for v in clothes_map.values()]
    for i in range(len(data_list)):
        for j in range(i, len(data_list)):
            answer += len(list(itertools.product(*data_list[i:j + 1])))

    return answer


def solution2(clothes: list[list[str]]) -> int:
    clothes_dict = defaultdict(list)
    for name, type_ in clothes:
        clothes_dict[type_].append(name)

    combinations = 1
    for type_ in clothes_dict:
        combinations *= (len(clothes_dict[type_]) + 1)

    return combinations - 1


if __name__ == '__main__':
    assert solution(
        [
            ["yellow_hat", "headgear"],
            ["blue_sunglasses", "eyewear"],
            ["green_turban", "headgear"],
        ],
    ) == 5
    assert solution(
        [
            ["crow_mask", "face"],
            ["blue_sunglasses", "face"],
            ["smoky_makeup", "face"],
        ],
    ) == 3

    assert solution2(
        [
            ["yellow_hat", "headgear"],
            ["blue_sunglasses", "eyewear"],
            ["green_turban", "headgear"],
        ],
    ) == 5
    assert solution2(
        [
            ["crow_mask", "face"],
            ["blue_sunglasses", "face"],
            ["smoky_makeup", "face"],
        ],
    ) == 3

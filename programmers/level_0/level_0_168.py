"""
최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다. 정수 배열 array가 매개변수로 주어질 때,
최빈값을 return 하도록 solution 함수를 완성해보세요. 최빈값이 여러 개면 -1을 return 합니다.

제한사항
- 0 < array의 길이 < 100
- 0 ≤ array의 원소 < 1000
"""
from utils import prvalue

from collections import Counter


@prvalue(print_result=False)
def solution(array: list[int]):
    most_commons = Counter(array).most_common(2)
    if len(most_commons) == 1:
        return most_commons[0][0]
    if most_commons[0][1] == most_commons[1][1]:
        return -1
    return most_commons[0][0]


if __name__ == '__main__':
    case1 = [1, 2, 3, 3, 3, 4]
    case2 = [1, 1, 2, 2]
    case3 = [1]
    case4 = [0]
    case5 = [0, 0]
    case6 = [0, 0, 1, 1, 1]

    assert solution(case1) == 3
    assert solution(case2) == -1
    assert solution(case3) == 1
    assert solution(case4) == 0
    assert solution(case5) == 0
    assert solution(case6) == 1

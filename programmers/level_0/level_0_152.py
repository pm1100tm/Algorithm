"""
등차수열 혹은 등비수열 common이 매개변수로 주어질 때, 마지막 원소 다음으로 올 숫자를 return 하도록
solution 함수를 완성해보세요.
"""
from utils import prvalue


@prvalue(print_result=False)
def solution(common: list[int]):
    x, y, z = common[0], common[1], common[2]
    if (y - x) == (z - y):
        return common[-1] + (y - x)
    else:
        return common[-1] * (y//x)


if __name__ == '__main__':
    assert solution([1, 2, 3, 4]) == 5
    assert solution([2, 4, 8]) == 16

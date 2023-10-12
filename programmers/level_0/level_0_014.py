"""
피자 나눠 먹기 (1)

머쓱이네 피자가게는 피자를 일곱 조각으로 잘라 줍니다.
피자를 나눠먹을 사람의 수 n이 주어질 때, 모든 사람이 피자를 한 조각 이상 먹기 위해 필요한 피자의 수를
return 하는 solution 함수를 완성해보세요.
"""
from utils import prvalue


@prvalue(print_time=True)
def solutio001(n: int):
    ret = divmod(n, 7)
    quo, rem = ret[0], ret[1]
    if not quo:
        return 1
    if not rem:
        return quo
    return quo + 1


@prvalue()
def solution002(n: int) -> int:
    ret = divmod(n, 7)
    return ret[0] + int(ret[1] != 0)


if __name__ == '__main__':
    # 7, 1
    # 1, 1
    # 15, 3
    pass

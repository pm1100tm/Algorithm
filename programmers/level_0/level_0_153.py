"""
양의 정수 n이 매개변수로 주어집니다. n × n 배열에 1부터 n2 까지 정수를 인덱스 [0][0]부터 시계방향
나선형으로 배치한 이차원 배열을 return 하는 solution 함수를 작성해 주세요.
1 ≤ n ≤ 30

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

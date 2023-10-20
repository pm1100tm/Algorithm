"""
정수 l과 r이 주어졌을 때, l 이상 r이하의 정수 중에서 숫자 "0"과 "5"로만 이루어진 모든 정수를
오름차순으로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.
만약 그러한 정수가 없다면, -1이 담긴 배열을 return 합니다.
"""
from utils import prvalue


@prvalue(print_result=False)
def solution(l, r):
    excludes = ['1', '2', '3', '4', '6', '7', '8', '9']

    def check_0_or_5(int_value):
        for char in str(int_value):
            if char in excludes:
                return False
        return True

    answer = [v for v in range(l, r + 1) if check_0_or_5(v)]

    return [-1] if not answer else answer


@prvalue(print_result=False)
def solution2(l, r):
    answer = [v for v in range(l, r + 1) if not set(str(v)) - {'0', '5'}]
    return [-1] if not answer else answer


if __name__ == '__main__':
    assert solution(5, 555) == [5, 50, 55, 500, 505, 550, 555]
    assert solution(10, 20) == [-1]
    assert solution2(5, 555) == [5, 50, 55, 500, 505, 550, 555]
    assert solution2(10, 20) == [-1]

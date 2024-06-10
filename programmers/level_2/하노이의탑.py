"""
몫 구하기

정수 num1, num2가 매개변수로 주어질 때, num1을 num2로 나눈 몫을 return 하도록
solution 함수를 완성해주세요.
"""
from utils import prvalue


@prvalue(print_result=False)
def solution(n: int):
    answer = []
    stack = [[_n for _n in range(n, 0, -1)], [], []]


if __name__ == '__main__':
    case1 = 2

    solution(case1)

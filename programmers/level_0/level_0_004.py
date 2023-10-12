"""
몫 구하기

정수 num1, num2가 매개변수로 주어질 때, num1을 num2로 나눈 몫을 return 하도록
solution 함수를 완성해주세요.
"""


def solution_001(num1: int, num2: int) -> int:
    return int(num1 / num2)


def solution_002(num1: int, num2: int) -> int:
    return num1 // num2


def solution_003(num1: int, num2: int) -> int:
    return divmod(num1, num2)[0]


def solution_004(num1: int, num2: int) -> int:
    solution = lambda x, y: x // y
    return solution(num1, num2)

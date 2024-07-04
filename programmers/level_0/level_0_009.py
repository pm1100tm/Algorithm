"""배열의 평균값
정수 배열 numbers가 매개변수로 주어집니다.
numbers의 원소의 평균값을 return하도록 solution 함수를 완성해주세요.
"""
from utils import prvalue


@prvalue(print_time=True)
def solution001(numbers: list[int]) -> float:
    div_number = len(numbers)
    return sum(numbers) / div_number


import statistics


@prvalue(print_time=True)
def solution002(numbers: list[int]) -> float:
    return statistics.mean(numbers)


if __name__ == '__main__':
    data = [n for n in range(1, 99999999)]
    solution001(data) # win
    solution002(data)

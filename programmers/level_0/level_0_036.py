"""
짝수는 싫어요

정수 n이 매개변수로 주어질 때, n 이하의 홀수가 오름차순으로 담긴 배열을 return하도록
solution 함수를 완성해주세요.
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(n: int):
    odd_int_list_under_n = [
        number
        for number in range(1, n + 1) if number % 2 != 0
    ]

    return sorted(odd_int_list_under_n)


@prvalue()
def solution001(n: int):
    return [number for number in range(1, n + 1, 2)]


@prvalue()
def solution002():
    pass


if __name__ == '__main__':
    assert solution(10) == [1, 3, 5, 7, 9]
    assert solution(15) == [1, 3, 5, 7, 9, 11, 13, 15]

    assert solution001(10) == [1, 3, 5, 7, 9]
    assert solution001(15) == [1, 3, 5, 7, 9, 11, 13, 15]

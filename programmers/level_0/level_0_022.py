"""
배열 자르기

정수 배열 numbers와 정수 num1, num2가 매개변수로 주어질 때,
numbers의 num1번 째 인덱스부터 num2번째 인덱스까지 자른 정수 배열을 return 하도록
solution 함수를 완성해보세요.
"""
from utils import prvalue


@prvalue()
def solution001(numbers: list[int], num1: int, num2: int) -> list[int]:
    return numbers[num1:num2 + 1]


if __name__ == '__main__':
    assert [2,3,4] == solution001([1, 2, 3, 4, 5], 1, 3)
    assert [3,5] == solution001([1, 3, 5], 1, 2)

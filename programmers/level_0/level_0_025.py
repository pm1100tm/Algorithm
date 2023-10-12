"""
배열 두배 만들기

정수 배열 numbers가 매개변수로 주어집니다.
numbers의 각 원소에 두배한 원소를 가진 배열을 return하도록 solution 함수를 완성해주세요.
"""
from utils import prvalue


@prvalue()
def solution(numbers: list[int]) -> list:
    return [n * 2 for n in numbers]


def solution001(numbers: list[int]):
    return list(map(lambda x: x * 2, numbers))


if __name__ == '__main__':
    assert solution([1, 2, 3, 4, 5]) == [2, 4, 6, 8, 10]
    assert solution([1, 2, 100, -99, 1, 2, 3]) == [2, 4, 200, -198, 2, 4, 6]
    assert solution([]) == []

    assert solution001([1, 2, 3, 4, 5]) == [2, 4, 6, 8, 10]
    assert solution001([1, 2, 100, -99, 1, 2, 3]) == [2, 4, 200, -198, 2, 4, 6]
    assert solution001([]) == []

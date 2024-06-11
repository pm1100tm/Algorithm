"""
정수 배열에 주어진 n 개의 연속되는 숫자가 존재하는지 판단한다.
- 정수 배열의 길이는 1 이상이다.
- 정수 배열은 중복되는 숫자가 존재한다.
- 정수 배열은 정렬되어있지 않다.
- 연속되는 숫자는 반드시 이어져있지 않아도 무방하다.
"""
from pytest import fixture


def is_consecutive_numbers_1(numbers: list[int], n: int) -> bool:
    """
    연속된 숫자의 갯수를 세는 방법
    """
    sorted_numbers = sorted(set(numbers))
    length = len(sorted_numbers)

    if length < n:
        return False

    count = 1
    result = False
    for i in range(length - 1):
        if sorted_numbers[i + 1] - sorted_numbers[i] != 1:
            count = 1
            continue

        count += 1
        if count == n:
            result = True
            break

    return result


def is_consecutive_numbers_2(numbers: list[int], n: int) -> bool:
    """
    연속되는 n 개의 정수 배열의 처음 값과 끝의 값을 뺀 값이 n - 1 라는 규칙을 이용한다.
    Sliding Window
    """
    sorted_number = sorted(set(numbers))

    if len(sorted_number) < n:
        return False

    for i in range(len(sorted_number) - n + 1):
        if sorted_number[i + n - 1] - sorted_number[i] == n - 1:
            return True

    return False


def is_consecutive_numbers_3(numbers: list[int], n: int) -> bool:
    """
    정수 num에 대해서 n 개의 연속되는 정수 배열을 만든 뒤, 각각의 원소가 배열에 존재하는지 판단한다.
    Hash Set
    """
    sorted_number = sorted(set(numbers))

    if len(sorted_number) < n:
        return False

    for num in numbers:
        if all([num + i in sorted_number for i in range(n)]):
            return True

    return False


@fixture()
def test_cases():
    return [
        ([1, 2, 3, 4, 5], 5, True),
        ([1, 3, 4, 5, 6, 7, 10], 5, True),
        ([1, 10, 11, 12, 14, 20, 21, 22, 23, 24, 30], 5, True),
        ([1, 10, 11, 12, 14, 20, 21, 22, 23, 25, 30], 5, False),
        ([1, 3, 5, 7, 10, 8], 2, True),
    ]


def test_is_consecutive_numbers(test_cases):
    for case in test_cases:
        assert (
            is_consecutive_numbers_1(case[0], case[1]) == case[2]
        ), 'Test Failed for is_consecutive_numbers_1'
        assert (
            is_consecutive_numbers_2(case[0], case[1]) == case[2]
        ), 'Test Failed for is_consecutive_numbers_2'
        assert (
            is_consecutive_numbers_3(case[0], case[1]) == case[2]
        ), 'Test Failed for is_consecutive_numbers_3'

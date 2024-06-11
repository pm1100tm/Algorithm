from typing import Deque
from collections import deque

from pytest import fixture


def is_palindrome_1(string: str) -> bool:
    if not string:
        return False

    strs = [char.lower() for char in string if char.isalnum()]

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True


def is_palindrome_2(string: str) -> bool:
    if not string:
        return False

    strs: Deque = deque()
    for char in string:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True


def is_palindrome_3(string: str) -> bool:
    if not string:
        return False

    strs = string.lower()
    return strs == strs[::-1]


@fixture()
def test_cases():
    return [
        ('test', False),
        ('as issi sa', True),
    ]


def test_is_palindrome_1(test_cases):
    for case in test_cases:
        assert is_palindrome_1(case[0]) is case[1]


def test_is_palindrome_2(test_cases):
    for case in test_cases:
        assert is_palindrome_2(case[0]) is case[1]


def test_is_palindrome_3(test_cases):
    for case in test_cases:
        assert is_palindrome_3(case[0]) is case[1]


if __name__ == '__main__':
    is_palindrome_2('as issi sa')

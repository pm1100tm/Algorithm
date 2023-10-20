"""
0 떼기

정수로 이루어진 문자열 n_str이 주어질 때,
n_str의 가장 왼쪽에 처음으로 등장하는 0들을 뗀 문자열을 return하도록 solution 함수를 완성해주세요.

2 ≤ n_str ≤ 10
n_str이 "0"으로만 이루어진 경우는 없습니다.
"""
from functools import reduce
from utils import prvalue


@prvalue()
def solution(n_str: str):
    """재귀로 풀기"""
    the_first_char = n_str[0]
    if int(the_first_char):
        return n_str

    return solution(n_str[1:])


@prvalue()
def solution001(n_str: str):
    """reduce 함수 사용하여 풀기"""
    def remove_zero(acc: str, char: str):
        if acc == '' and char == '0':
            return acc
        return acc + char

    return reduce(remove_zero, n_str, '')


@prvalue()
def solution002(n_str: str):
    """kingthod"""
    return n_str.lstrip("0")


if __name__ == '__main__':
    assert solution("0010") == "10"
    assert solution("854020") == "854020"
    assert solution001("0010") == "10"
    assert solution001("854020") == "854020"
    assert solution002("0010") == "10"
    assert solution002("854020") == "854020"

"""최댓값과 최솟값
https://school.programmers.co.kr/learn/courses/30/lessons/12939
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(s: str) -> str:
    numbers = [int(v) for v in s.split(' ')]
    return f'{min(numbers)} {max(numbers)}'


if __name__ == '__main__':
    assert solution('1 2 3 4') == '1 4'
    assert solution('-1 -2 -3 -4') == '-4 -1'
    assert solution('-1 -1') == '-1 -1'

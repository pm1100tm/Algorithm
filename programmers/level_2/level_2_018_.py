"""예상 대진표
https://school.programmers.co.kr/learn/courses/30/lessons/12985
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(n: int, a: int, b: int) -> int:
    def convert_to_last_num(num: int) -> int:
        return num if num % 2 == 0 else num + 1

    def get_next_round_last_num(num: int) -> int:
        return convert_to_last_num(num // 2)

    r = 1
    na = convert_to_last_num(a)
    nb = convert_to_last_num(b)

    while abs(na - nb) > 0:
        r += 1
        na = get_next_round_last_num(na)
        nb = get_next_round_last_num(nb)

    return r


if __name__ == '__main__':
    assert solution(8, 4, 7) == 3
    assert solution(2, 1, 2) == 1
    assert solution(8, 1, 3) == 2
    assert solution(1048576, 12345, 12346) == 1
    assert solution(8, 5, 8) == 2
    assert solution(4, 2, 3) == 2

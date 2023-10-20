"""
세균 증식

어떤 세균은 1시간에 두배만큼 증식한다고 합니다.
처음 세균의 마리수 n과 경과한 시간 t가 매개변수로 주어질 때
t시간 후 세균의 수를 return하도록 solution 함수를 완성해주세요.

1 ≤ n ≤ 10
1 ≤ t ≤ 15
"""
from utils import prvalue


@prvalue(print_time=True)
def solution(n: int, t: int) -> int:
    answer = n

    def squre_n(x: int):
        nonlocal answer
        answer = x * 2

    [squre_n(answer) for _t in range(1, t + 1)]

    return answer


@prvalue(print_time=True)
def solution001(n: int, t: int) -> int:
    answer = n
    for _t in range(1, t + 1):
        answer = answer * 2

    return answer


@prvalue(print_time=True)
def solution002(n: int, t: int) -> int:
    answer = n ** 2 * t
    return answer


if __name__ == '__main__':
    assert solution(2, 10) == 2048
    assert solution(7, 15) == 229376

    assert solution001(2, 10) == 2048
    assert solution001(7, 15) == 229376

    solution(17, 200000)
    solution001(17, 200000)
    solution002(17, 200000)

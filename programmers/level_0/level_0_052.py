"""
수 조작하기 1

정수 n과 문자열 control이 주어집니다.
control은 "w", "a", "s", "d"의 4개의 문자로 이루어져 있으며,
control의 앞에서부터 순서대로 문자에 따라 n의 값을 바꿉니다.
"w" : n이 1 커집니다.
"s" : n이 1 작아집니다.
"d" : n이 10 커집니다.
"a" : n이 10 작아집니다.
위 규칙에 따라 n을 바꿨을 때 가장 마지막에 나오는 n의 값을 return 하는 solution 함수를 완성해 주세요.

-100,000 ≤ n ≤ 100,000
1 ≤ control의 길이 ≤ 100,000
control은 알파벳 소문자 "w", "a", "s", "d"로 이루어진 문자열입니다.
"""
from functools import reduce
from utils import prvalue


@prvalue(print_time=True)
def solution(n, control: str) -> int:
    cal = {
        "w": lambda x: x + 1,
        "s": lambda x: x - 1,
        "d": lambda x: x + 10,
        "a": lambda x: x - 10,
    }

    for c in control:
        n = cal[c](n)

    return n


@prvalue(print_time=True)
def solution001(n, control: str) -> int:
    key = dict(zip(['w', 's', 'd', 'a'], [1, -1, 10, -10]))
    return n + sum([key[c] for c in control])


@prvalue(print_result=True)
def solution002(n, control: str) -> int:
    cal = sum(
        [
            control.count("w") * 1,
            control.count("s") * -1,
            control.count("d") * 10,
            control.count("a") * -10,
        ]
    )

    return n + cal


if __name__ == '__main__':
    _control = "wsdawsdassww" * 5000000
    assert solution(0, _control) == 0
    assert solution001(0, _control) == 0
    assert solution002(0, _control) == 0
    assert solution002(0, "wsdawsdassw") == -1
    assert solution002(0, _control) == 0

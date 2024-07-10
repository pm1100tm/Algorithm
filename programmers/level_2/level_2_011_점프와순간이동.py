"""점프와 순간 이동
https://school.programmers.co.kr/learn/courses/30/lessons/12980
- idea
목표거리 n을 2진수로 표현하면, 2진수 표현의 각 비트를 스킬을 사용할 결정점으로 생각할 수 있다.
즉, 1이란 0에서 1로 가기위한 횟수이며, 이것은 베터리 사용량(1)과 같다.
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(n: int) -> int:
    bin_n = str(bin(n))[2:]
    return bin_n.count('1')


if __name__ == '__main__':
    assert solution(4) == 1
    assert solution(5) == 2
    assert solution(6) == 2
    assert solution(7) == 3
    assert solution(8) == 1
    assert solution(5000) == 5

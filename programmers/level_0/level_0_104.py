"""
369게임

머쓱이는 친구들과 369게임을 하고 있습니다.
369게임은 1부터 숫자를 하나씩 대며 3, 6, 9가 들어가는 숫자는 숫자 대신 3, 6, 9의 개수만큼
박수를 치는 게임입니다. 머쓱이가 말해야하는 숫자 order가 매개변수로 주어질 때,
머쓱이가 쳐야할 박수 횟수를 return 하도록 solution 함수를 완성해보세요.

1 ≤ order ≤ 1,000,000

3	1
29423	2
"""
from collections import Counter
from utils import prvalue


@prvalue(print_result=True)
def solution(order: int) -> int:
    res = Counter(str(order))
    return res.get("3", 0) + res.get("6", 0) + res.get("9", 0)


if __name__ == '__main__':
    assert solution(3) == 1
    assert solution(29423) == 2
    assert solution(33333333333333) == 14
    assert solution(36936911111111) == 6

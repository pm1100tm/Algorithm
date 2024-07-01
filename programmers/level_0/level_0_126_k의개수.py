"""k의 개수

1부터 13까지의 수에서, 1은 1, 10, 11, 12, 13 이렇게 총 6번 등장합니다.
정수 i, j, k가 매개변수로 주어질 때, i부터 j까지 k가 몇 번 등장하는지 return
하도록 solution 함수를 완성해주세요.

1 ≤ i < j ≤ 100,000
0 ≤ k ≤ 9

1	13	1	6
10	50	5	5
3	10	2	0
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(i, j, k):
    """
    count와 같은 처리는 한 번에 하는 것이 효율적이다.
    """
    n_string = ""
    for n in range(i, j + 1):
        n_string += str(n)

    return n_string.count(str(k))


if __name__ == '__main__':
    solution(1, 13, 1)
    solution(10, 50, 5)
    solution(3, 10, 2)


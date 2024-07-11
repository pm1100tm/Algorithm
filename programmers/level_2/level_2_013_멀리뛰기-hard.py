"""멀리 뛰기
https://school.programmers.co.kr/learn/courses/30/lessons/12914
- idea: DP
동적 프로그래밍을 사용하여 해결할 수 있는 고전적인 문제
특정 공간에 도달하는 방법의 수는 이전 두 공간에 도달하는 방법의 합이라는 점에서 피보나치 수열과 유사하다.
n번째 공간에 도달하는 방법의 수를 구하기 위해, (n-1)번째 공간 또는 (n-2)번째 공간에서 왔을 수 있다는
사실을 이용한다.
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(n: int) -> int:
    if n <= 1:
        return 1

    ways = [0] * (n + 1)

    ways[0] = 1
    ways[1] = 1

    for i in range(2, n + 1):
        ways[i] = ways[i - 1] + ways[i - 2]

    return ways[n] % 1234567


if __name__ == '__main__':
    solution(4)
    solution(3)

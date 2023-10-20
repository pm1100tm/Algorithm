"""
팩토리얼

i팩토리얼 (i!)은 1부터 i까지 정수의 곱을 의미합니다.
예를들어 5! = 5 * 4 * 3 * 2 * 1 = 120 입니다.
정수 n이 주어질 때 다음 조건을 만족하는 가장 큰 정수 i를 return 하도록 solution 함수를 완성해주세요.

i! ≤ n

0 < n ≤ 3,628,800

3628800	10
7	3
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(n):
    def factorial(_n):
        result = 1
        for i in range(2, _n + 1):
            result *= i
        return result

    for num in range(2, n + 1):
        ret = factorial(num)
        if ret >= n:
            if ret == n:
                return num
            else:
                return num - 1

    return n


@prvalue(print_result=True)
def solution001(n):
    from math import factorial

    k = 10
    while n < factorial(k):
        k -= 1

    return k


@prvalue(print_result=True)
def solution002(n: int):
    answer = 1
    factorial = 1
    while factorial <= n:
        answer += 1
        factorial *= answer

    return answer - 1


if __name__ == '__main__':
    solution(7)
    solution(3628800)
    solution001(7)
    solution001(3628800)
    solution002(7)
    solution002(3628800)

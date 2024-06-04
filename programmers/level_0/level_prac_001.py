"""
피보나치 수는 F(0) = 0, F(1) = 1일 때, 1 이상의 n에 대하여 F(n) = F(n-1) + F(n-2) 가 적용되는 수
입니다. 예를들어
- F(2) = F(0) + F(1) = 0 + 1 = 1
- F(3) = F(1) + F(2) = 1 + 1 = 2
- F(4) = F(2) + F(3) = 1 + 2 = 3
- F(5) = F(3) + F(4) = 2 + 3 = 5

와 같이 이어집니다. 2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는
함수, solution을 완성해 주세요.

제한 사항
- n은 2 이상 100,000 이하인 자연수입니다.

피보나치수는 0번째부터 0, 1, 1, 2, 3, 5, ... 와 같이 이어집니다.
"""
from utils import prvalue


@prvalue(print_result=False)
def solution(n):
    CONST_MOD = 1234567

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b % CONST_MOD


def prac_to_make_fibonacci_nubmer_list_method1(n: int):
    if n == 0:
        return [0]
    if n == 1:
        return [0, 1]

    fibo_list: list[int] = [0, 1]
    for _ in range(2, n + 1):
        fibo_list.append(fibo_list[-2] + fibo_list[-1])

    return fibo_list


def prac_to_make_fibonacci_nubmer_list_method2(n: int) -> list[int]:

    def fibo_recursive(_n: int):
        if _n == 0:
            return 0
        if _n == 1:
            return 1

        return fibo_recursive(_n - 2) + fibo_recursive(_n - 1)

    def generate_fibo_recursive(_n: int) -> list[int]:
        return [fibo_recursive(i) for i in range(_n + 1)]

    return generate_fibo_recursive(n)


if __name__ == '__main__':
    # assert solution(3) == 2
    # assert solution(5) == 5
    print(prac_to_make_fibonacci_nubmer_list_method1(10))
    print(prac_to_make_fibonacci_nubmer_list_method2(10))

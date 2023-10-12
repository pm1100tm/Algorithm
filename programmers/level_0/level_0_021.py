"""
순서쌍의 개수

순서쌍이란 두 개의 숫자를 순서를 정하여 짝지어 나타낸 쌍으로 (a, b)로 표기합니다.
자연수 n이 매개변수로 주어질 때 두 숫자의 곱이 n인 자연수 순서쌍의 개수를 return하도록
solution 함수를 완성해주세요.
"""
from utils import prvalue


@prvalue(print_time=True)
def solution001(n) -> int:
    if n == 1:
        return 1
    if n == 2 or n == 3:
        return 2

    count = 2
    for i in range(2, int(n/2) + 1):
        remains = divmod(n , i)[-1]
        if remains == 0:
            count += 1

    return count


@prvalue(print_time=True)
def solution002(n) -> int:
    if n == 1:
        return 1
    if n == 2 or n == 3:
        return 2

    count = sum([1 for i in range(2, int(n / 2) + 1) if n % i == 0]) + 2

    return count


@prvalue(print_time=True)
def solution003(n) -> int:
    if n == 1:
        return 1
    if n == 2 or n == 3:
        return 2

    count = len([1 for i in range(2, int(n / 2) + 1) if n % i == 0]) + 2

    return count


@prvalue(print_time=True)
def solution004(n) -> int:
    answer = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            answer += 2

            if i * i == n:
                answer -= 1

    return answer


if __name__ == '__main__':
    # for n in range(1, 101):
    #     r = int(n ** 0.5)
    #     print(f"{n} : {r * r}")
    pass

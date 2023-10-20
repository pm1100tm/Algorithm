"""
약수 구하기

정수 n이 매개변수로 주어질 때, n의 약수를 오름차순으로 담은 배열을 return하도록 solution 함수를 완성해주세요.
1 ≤ n ≤ 10,000

24	[1, 2, 3, 4, 6, 8, 12, 24]
29	[1, 29]
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(n: int):
    divisors: list[int] = []
    for number in range(1, int(n ** 0.5) + 1):
        if n % number == 0:
            divisors.append(number)
            if number != n // number:
                divisors.append(n // number)

    divisors.sort()

    return divisors


if __name__ == '__main__':
    assert solution(24) == [1, 2, 3, 4, 6, 8, 12, 24]
    assert solution(29) == [1, 29]

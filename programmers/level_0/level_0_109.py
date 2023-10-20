"""
합성수 찾기

약수의 개수가 세 개 이상인 수를 합성수라고 합니다.
자연수 n이 매개변수로 주어질 때 n이하의 합성수의 개수를 return하도록 solution 함수를 완성해주세요.

1 ≤ n ≤ 100

10	5
15	8
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(n: int):

    def get_divisor_n_number(_n: int) -> int:
        count = 0
        for i in range(1, int(_n ** 0.5) + 1):
            if _n % i == 0:
                count += 1 if i == _n // i else 2

        return count

    divisor_num = [
        1
        for i in range(1, n + 1)
        if get_divisor_n_number(i) > 2
    ]

    return sum(divisor_num)


if __name__ == '__main__':
    solution(15)

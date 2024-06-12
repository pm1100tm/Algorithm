"""소수 찾기
1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.
소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다. (1은 소수가 아닙니다.)

제한 조건
- n은 2이상 1000000이하의 자연수입니다.

n   result
10  4
5   3
"""


def is_prime(n):
    if n <= 1:
        return False

    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True


def solution(n: int) -> int:
    count = 0
    for number in range(2, n + 1):
        if is_prime(number):
            count += 1

    return count


if __name__ == '__main__':
    assert solution(10) == 4
    assert solution(5) == 3

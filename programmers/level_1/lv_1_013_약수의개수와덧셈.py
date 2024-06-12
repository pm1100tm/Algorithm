"""약수의 개수와 덧셈
두 정수 left와 right가 매개변수로 주어집니다. left부터 right까지의 모든 수들 중에서, 약수의 개수가
짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.

제한사항
- 1 ≤ left ≤ right ≤ 1,000
"""


def count_divisors(n: int):
    if n <= 0:
        raise ValueError("n must be a positive integer")

    count = 0
    sqrt_n = int(n ** 0.5)

    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            count += 1
            if i != n // i:
                count += 1

    return count


def solution(left: int, right: int) -> int:
    answer = 0
    for n in range(left, right + 1):
        if count_divisors(n) % 2 == 0:
            answer += n
        else:
            answer -= n

    return answer


if __name__ == '__main__':
    assert solution(13, 17) == 43
    assert solution(24, 27) == 52

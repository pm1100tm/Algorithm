"""소수만들기
"""
from itertools import combinations


def is_prime(n) -> bool:
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


def solution(nums: list[int]) -> int:
    answer = 0

    for com in combinations(set(nums), 3):
        if is_prime(sum(com)):
            answer += 1
    print(answer)
    return answer


if __name__ == '__main__':
    solution([1, 2, 3, 4])
    solution([1,2,7,6,4])
    # assert solution([1,2,3,4]) == 1

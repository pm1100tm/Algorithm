"""숫자의 표현
https://school.programmers.co.kr/learn/courses/30/lessons/12924
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(n: int):
    if n == 1 or n == 2:
        return 1

    answer = 0
    for i in range(1, (n // 2 + 1) + 1):
        nums = [i]
        while nums[-1] < (n // 2 + 1) + 1:
            total = sum(nums)
            if total > n:
                break

            if total == n:
                answer += 1
                break

            last_n = nums[-1]
            nums.append(last_n + 1)

    return answer + 1


if __name__ == '__main__':
    assert solution(15) == 4

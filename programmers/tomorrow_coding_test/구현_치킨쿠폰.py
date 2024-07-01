"""치킨쿠폰
https://school.programmers.co.kr/tryouts/85900/challenges
"""


def solution(chicken: int):
    N = 10
    answer = 0
    coupons = chicken

    while coupons >= N:
        quo, rem = divmod(coupons, N)
        answer += quo
        coupons = quo + rem

    return answer


if __name__ == '__main__':
    assert solution(100) == 11
    assert solution(1081) == 120

"""369게임
https://school.programmers.co.kr/tryouts/85902/challenges
"""


def solution(order: int):
    answer = 0
    char_list = ['3', '6', '9']
    for c in char_list:
        answer += str(order).count(c)

    return answer


if __name__ == '__main__':
    assert solution(3) == 1
    assert solution(29423) == 2

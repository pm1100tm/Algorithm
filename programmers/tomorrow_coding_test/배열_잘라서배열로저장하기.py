"""7의 개수
https://school.programmers.co.kr/tryouts/85905/challenges?language=python3
"""


def solution(my_str: str, n: int):
    index = 0
    answer = []
    while index < len(my_str):
        answer.append(my_str[index : index + n])
        index += n

    return answer


if __name__ == '__main__':
    assert solution('abc1Addfggg4556b', 6) == ["abc1Ad", "dfggg4", "556b"]

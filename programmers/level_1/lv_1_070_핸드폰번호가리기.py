"""핸드폰 번호 가리기
https://school.programmers.co.kr/learn/courses/30/lessons/12948
"""
import re


def solution(phone_number: str) -> str:
    temp = phone_number[-4::]
    stars = re.sub('[0-9]', '*', phone_number[0:-4])

    return stars + temp


def solution2(phone_number: str) -> str:
    return '*' * (len(phone_number) - 4) + phone_number[-4:]


if __name__ == '__main__':
    assert solution('01033334444') == '*******4444'
    assert solution('027778888') == '*****8888'
    assert solution2('01033334444') == '*******4444'
    assert solution2('027778888') == '*****8888'

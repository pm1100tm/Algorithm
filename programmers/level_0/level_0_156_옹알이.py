"""옹알이
https://school.programmers.co.kr/learn/courses/30/lessons/120956
"""
from utils import prvalue


@prvalue(print_result=False)
def solution(babbling):
    str_list = babbling[:]
    words = ["aya", "ye", "woo", "ma"]

    count = 0
    for s in str_list:
        for w in words:
            s = s.replace(w, ' ')
        if not s.replace(' ', ''):
            count += 1

    return count


import re


def solution2(babbling: list[str]):
    regex = re.compile('^(aya|ye|woo|ma)+$')
    count = 0
    for b in babbling:
        if regex.match(b):
            count += 1
    return count


def solution3(babbling: list[str]) -> int:
    answer = 0
    words = ["aya", "ye", "woo", "ma"]

    for b in babbling:
        temp = ''
        flag = False
        for char in b:
            temp += char
            if temp in words:
                if b.count(temp) == 1:
                    flag = True
                temp = ''

        if not temp and flag:
            answer += 1

    return answer


if __name__ == '__main__':
    assert solution(["aya", "yee", "u", "maa", "wyeoo"]) == 1
    assert solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]) == 3
    assert solution(["aye"]) == 0

    assert solution2(["aya", "yee", "u", "maa", "wyeoo"]) == 1
    assert solution2(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]) == 3
    assert solution2(["aye"]) == 0

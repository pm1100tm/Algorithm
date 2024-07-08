"""옹알이(2)
https://school.programmers.co.kr/learn/courses/30/lessons/133499
Idea: string manipulation
"""
import re


def solution(babbling: list[str]) -> int:
    words = ["aya", "ye", "woo", "ma"]
    pattern = re.compile('^(aya|ye|woo|ma)+$')
    answer = 0
    for b in babbling:
        if pattern.match(b) and not any([b.count(w*2) for w in words]):
            answer += 1

    return answer


def solution2(babbling: list[str]) -> int:
    words = ["aya", "ye", "woo", "ma"]
    count = 0
    for b in babbling:
        comp, temp = '', ''

        for char in b:
            comp += char

            if comp == temp:
                break

            if comp in words:
                temp = comp
                comp = ''

        if not comp:
            count += 1

    return count


def solution3(babbling: list[str]) -> int:
    valid_pattern = re.compile(r'^(?!.*(aya|ye|woo|ma)\1)(aya|ye|woo|ma)+$')
    count = 0

    for word in babbling:
        if valid_pattern.fullmatch(word):
            count += 1

    return count


if __name__ == '__main__':
    assert solution(["aya", "yee", "u", "maa"]) == 1
    assert solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]) == 2
    assert solution2(["aya", "yee", "u", "maa"]) == 1
    assert solution2(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]) == 2
    assert solution3(["aya", "yee", "u", "maa"]) == 1
    assert solution3(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]) == 2


"""다트게임
https://school.programmers.co.kr/learn/courses/30/lessons/17682
"""
import re


def solution(dart_result: str) -> int:
    num = ''
    check_count = -1
    scores = [0] * 3

    for char in dart_result:
        if char.isdigit():
            num += char
            continue

        if num:
            check_count += 1
            scores[check_count] = int(num)
            num = ''

        if char == 'S':
            scores[check_count] = scores[check_count] ** 1
            continue

        if char == 'D':
            scores[check_count] = scores[check_count] ** 2
            continue

        if char == 'T':
            scores[check_count] = scores[check_count] ** 3
            continue

        if char == '*':
            scores[check_count] = scores[check_count] * 2

            if check_count > 0:
                scores[check_count - 1] = scores[check_count - 1] * 2

            continue

        if char == '#':
            scores[check_count] = scores[check_count] * -1

    return sum(scores)


def solution2(dart_result: str) -> int:
    bonus = {'S': 1, 'D': 2, 'T': 3}
    option = {'': 1, '*': 2, '#': -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dart_result)

    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i - 1] *= 2

        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    return sum(dart)


if __name__ == '__main__':
    assert solution('1S2D*3T') == 37
    assert solution('1D2S#10S') == 9
    assert solution('1D2S0T') == 3
    assert solution('1S*2T*3S') == 23
    assert solution('1D#2S*3S') == 5
    assert solution('1T2D3D#') == -4
    assert solution('1D2S3T*') == 59

    assert solution2('1S2D*3T') == 37
    assert solution2('1D2S#10S') == 9
    assert solution2('1D2S0T') == 3
    assert solution2('1S*2T*3S') == 23
    assert solution2('1D#2S*3S') == 5
    assert solution2('1T2D3D#') == -4
    assert solution2('1D2S3T*') == 59

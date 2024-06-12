"""문자열 내 p와 y의 개수

대문자와 소문자가 섞여있는 문자열 s가 주어집니다. s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True,
다르면 False를 return 하는 solution를 완성하세요.
- 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다.
- 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.
- 예를 들어 s가 pPoooyY면 true를 return하고 Pyy라면 false를 return합니다.

제한사항
- 문자열 s의 길이 : 50 이하의 자연수
- 문자열 s는 알파벳으로만 이루어져 있습니다.
"""
from collections import Counter


def solution(s: str) -> bool:
    char_map = {'p': 0, 'y': 0}

    for _s in s.lower():
        if _s.lower() in char_map:
            char_map[_s] += 1

    return char_map['p'] == char_map['y']


def solution2(s: str) -> bool:
    return s.lower().count('p') == s.lower().count('y')


def solution3(s: str) -> bool:
    count_map = Counter(s.lower())

    return count_map['p'] == count_map['y']


if __name__ == '__main__':
    cases = [
        ('pPooooooooooyY', True),
        ('Pyyyyyyyyyyyy', False),
        ('aaaaaaaaaabbbbbbbb', True),
    ]

    for case in cases:
        assert solution(case[0]) == case[1]
        assert solution2(case[0]) == case[1]
        assert solution3(case[0]) == case[1]

"""시저 암호
https://school.programmers.co.kr/learn/courses/30/lessons/12926
"""


def solution(s: str, n: int) -> str:
    # 대: 65 ~ 90, 소: 97 ~ 122
    answer = ''
    for char in s:
        if char == ' ':
            answer += char
            continue

        if char.islower():
            x, y = divmod(ord(char) + n, 122)
            if not x:
                answer += chr(y)
            else:
                answer += chr(97 + y - 1)
        else:
            x, y = divmod(ord(char) + n, 90)
            if not x:
                answer += chr(y)
            else:
                answer += chr(65 + y - 1)

    return answer


def solution2(s, n):
    s = list(s)

    for i in range(len(s)):
        if s[i] == ' ':
            s[i] = ' '
            continue
        if s[i].isupper():
            s[i] = chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))
        else:
            s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))

    return ''.join(s)


if __name__ == '__main__':
    assert solution('AB', 1) == 'BC'
    assert solution('z', 1) == 'a'
    assert solution('a B z', 4) == 'e F d'
    assert solution2('AB', 1) == 'BC'
    assert solution2('z', 1) == 'a'
    assert solution2('a B z', 4) == 'e F d'

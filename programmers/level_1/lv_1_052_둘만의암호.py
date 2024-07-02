"""둘만의암호
https://school.programmers.co.kr/learn/courses/30/lessons/155652
"""
from string import ascii_lowercase


def solution(s: str, skip: str, index: int):
    answer = ''

    for char in s:
        count = 0
        temp = char

        while count < index:
            next_char = chr((ord(temp) + 1 - ord('a')) % 26 + ord('a'))
            if next_char not in skip:
                count += 1

            temp = next_char

        answer += temp

    return answer


def solution2(s: str, skip: str, index: int):
    a_to_z = sorted(set(ascii_lowercase) - set(skip))
    a_to_z_len = len(a_to_z)
    new_alpha_dict = {char:index for index, char in enumerate(a_to_z)}

    answer = ''
    for char in s:
        answer += a_to_z[(new_alpha_dict[char] + index) % a_to_z_len]

    return answer


if __name__ == '__main__':
    assert solution('aukks', 'wbqd', 5) == 'happy'
    assert solution('z', 'a', 1) == 'b'
    assert solution("a", "bcdefghijk", 20) == "o"
    assert solution("z", "abcdefghij", 20) == "n"
    assert solution("aukks", "wbqd", 5) == "happy"
    assert solution("abcde", "bcd", 2) == "ffffg"
    assert solution("yyyyy", "za", 2) == "ccccc"
    assert solution("ybcde", "az", 1) == "bcdef"
    assert solution("zzzzzz", "abcdefghijklmnopqrstuvwxy", 6) == "zzzzzz"
    assert solution("bcdefghijklmnopqrstuvwxyz", "a", 1) == "cdefghijklmnopqrstuvwxyzb"

    assert solution2('aukks', 'wbqd', 5) == 'happy'

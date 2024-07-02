"""둘만의 암호
https://school.programmers.co.kr/tryouts/85924/challenges?language=python3
"""
from string import ascii_lowercase


def solution(s: str, skip: str, index: int) -> str:
    a_ord: int = ord('a')
    answer = ''

    for char in s:
        count = 1
        char_list = []
        while len(char_list) < index:
            shiftd_ord_value: int = (ord(char) + count - a_ord) % 26 + a_ord
            last_char = chr(shiftd_ord_value)
            if last_char in skip:
                count += 1
                continue

            char_list.append(last_char)
            count += 1

        assert len(char_list) == 5
        answer += char_list[-1]

    return answer


def solution2(s: str, skip: str, index: int):
    letters = sorted(set(ascii_lowercase) - set(skip))
    letters_len = len(letters)
    letters_dic = {char:index for index, char in enumerate(letters)}

    answer = ''
    for char in s:
        i = (letters_dic[char] + index) % letters_len
        answer += letters[i]

    return answer


if __name__ == '__main__':
    assert solution("aukks", "wbqd", 5) == 'happy'
    assert solution2("aukks", "wbqd", 5) == 'happy'

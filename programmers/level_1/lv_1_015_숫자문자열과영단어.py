"""숫자 문자열과 영단어(카카오2021)
"""


def solution(s: str) -> int:
    number_map = {
        "zero" : "0",
        "one"  : "1",
        "two"  : "2",
        "three": "3",
        "four" : "4",
        "five" : "5",
        "six"  : "6",
        "seven": "7",
        "eight": "8",
        "nine" : "9",
    }

    answer = ''
    n_str = ''
    for i, char in enumerate(s):
        if char.isdigit():
            answer += char
        else:
            n_str += char
            ret = number_map.get(n_str)
            if ret:
                answer += ret
                n_str = ''

    return int(answer)


def solution2(s: str) -> int:
    number_words = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]

    answer = s
    for i, w in enumerate(number_words):
        answer = answer.replace(w, str(i))

    assert answer.isdigit()
    return int(answer)


if __name__ == '__main__':
    assert solution('one4seveneight') == 1478
    assert solution('23four5six7') == 234567
    assert solution('2three45sixseven') == 234567
    assert solution('123') == 123

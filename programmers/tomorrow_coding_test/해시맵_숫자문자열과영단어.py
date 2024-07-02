"""숫자 문자열과 영단어
https://school.programmers.co.kr/tryouts/85915/challenges?language=python3
"""


def solution(s: str):
    number_map = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }

    answer = ''
    n_str = ''
    for char in s:
        if char.isdigit():
            answer += char
        else:
            n_str += char
            if number_map.get(n_str):
                answer += number_map.get(n_str)
                n_str = ''

    return int(answer)


def solution2(s: str):
    number_word = [
        'zero',
        'one',
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven',
        'eight',
        'nine',
    ]

    answer = s
    for i, w in enumerate(number_word):
        answer = answer.replace(w, str(i))

    return int(answer)


if __name__ == '__main__':
    assert solution('one4seveneight') == 1478
    assert solution('23four5six7') == 234567
    assert solution('2three45sixseven') == 234567
    assert solution('123') == 123

    assert solution2('one4seveneight') == 1478
    assert solution2('23four5six7') == 234567
    assert solution2('2three45sixseven') == 234567
    assert solution2('123') == 123

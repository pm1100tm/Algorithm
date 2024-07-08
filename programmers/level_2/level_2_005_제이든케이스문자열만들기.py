"""JadenCase 문자열 만들기
https://school.programmers.co.kr/learn/courses/30/lessons/12951
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(s: str) -> str:
    answer = []
    temp_chars = ''

    def convert_chars(chars: str) -> str:
        if chars[0].isalpha():
            return chars[0].upper() + chars[1:].lower()
        else:
            return chars.lower()

    for char in s:
        if char == ' ':
            if temp_chars:
                answer.append(convert_chars(temp_chars))
                temp_chars = ''
            answer.append(' ')

        else:
            temp_chars += char

    if temp_chars:
        answer.append(convert_chars(temp_chars))

    return ''.join(answer)


@prvalue(print_result=True)
def solution2(s: str) -> str:
    words = s.split(' ')
    jaden_case_words = []
    for word in words:
        if word:
            jaden_case_words.append(word[0].upper() + word[1:].lower())
        else:
            jaden_case_words.append(word)

    return ' '.join(jaden_case_words)


if __name__ == '__main__':
    assert solution("3people unFollowed me") == "3people Unfollowed Me"
    assert solution("for the last week") == "For The Last Week"
    assert solution("AAAA") == 'Aaaa'
    assert solution("AAAA bAA  1AAA") == 'Aaaa Baa  1aaa'
    assert solution("  multiple   spaces") == '  Multiple   Spaces'

    assert solution2("3people unFollowed me") == "3people Unfollowed Me"
    assert solution2("for the last week") == "For The Last Week"
    assert solution2("AAAA") == 'Aaaa'
    assert solution2("AAAA bAA  1AAA") == 'Aaaa Baa  1aaa'
    assert solution2("  multiple   spaces") == '  Multiple   Spaces'

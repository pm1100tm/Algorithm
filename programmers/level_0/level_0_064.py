"""
l로 만들기

알파벳 소문자로 이루어진 문자열 myString이 주어집니다.
알파벳 순서에서 "l"보다 앞서는 모든 문자를 "l"로 바꾼 문자열을 return 하는 solution 함수를 완성해 주세요.

1 ≤ myString ≤ 100,000
myString은 알파벳 소문자로 이루어진 문자열입니다.
"""
from utils import prvalue


@prvalue(print_time=True)
def solution(my_string: str):
    return ''.join(map(lambda x: 'l' if x < 'l' else x, my_string))


@prvalue(print_time=True)
def solution001(my_string: str):
    return my_string.translate(str.maketrans('abcdefghijk', 'lllllllllll'))


@prvalue(print_time=True)
def solution002(my_string: str):
    lower_l = "l"
    return "".join([lower_l if s < lower_l else s for s in my_string])


if __name__ == '__main__':
    assert solution("abcdevwxyz") == "lllllvwxyz"
    assert solution("jjnnllkkmm") == "llnnllllmm"

    assert solution001("abcdevwxyz") == "lllllvwxyz"
    assert solution001("jjnnllkkmm") == "llnnllllmm"

    assert solution002("abcdevwxyz") == "lllllvwxyz"
    assert solution002("jjnnllkkmm") == "llnnllllmm"

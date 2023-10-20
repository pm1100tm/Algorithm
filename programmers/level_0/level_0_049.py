"""
특정한 문자를 대문자로 바꾸기

영소문자로 이루어진 문자열 my_string과 영소문자 1글자로 이루어진 문자열 alp가 매개변수로 주어질 때,
my_string에서 alp에 해당하는 모든 글자를 대문자로 바꾼 문자열을 return 하는 solution 함수를 작성해 주세요.

1 ≤ my_string의 길이 ≤ 1,000
"""
import re

from utils import prvalue


@prvalue(print_result=True)
def solution(my_string: str, alp: str):
    index: int = my_string.find(alp)
    if index == -1:
        return my_string

    char_list = [x for x in my_string]
    char_list[index] = char_list[index].upper()

    return solution("".join(char_list), alp)


@prvalue()
def solution001(my_string: str, alp: str):
    pattern = re.compile(re.escape(alp))
    return pattern.sub(alp.upper(), my_string)


@prvalue()
def solution002(my_string: str, alp: str):
    return my_string.replace(alp, alp.upper())


if __name__ == '__main__':
    assert solution("hello world", "o") == "hellO wOrld"
    assert solution("programmers", "p") == "Programmers"
    assert solution("lowercase", "x") == "lowercase"

    assert solution001("hello world", "o") == "hellO wOrld"
    assert solution001("programmers", "p") == "Programmers"
    assert solution001("lowercase", "x") == "lowercase"

    assert solution002("hello world", "o") == "hellO wOrld"
    assert solution002("programmers", "p") == "Programmers"
    assert solution002("lowercase", "x") == "lowercase"

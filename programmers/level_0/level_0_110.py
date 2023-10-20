"""
중복된 문자 제거

문자열 my_string이 매개변수로 주어집니다.
my_string에서 중복된 문자를 제거하고 하나의 문자만 남긴 문자열을 return하도록 solution 함수를 완성해주세요.

1 ≤ my_string ≤ 110
my_string은 대문자, 소문자, 공백으로 구성되어 있습니다.
대문자와 소문자를 구분합니다.
공백(" ")도 하나의 문자로 구분합니다.
중복된 문자 중 가장 앞에 있는 문자를 남깁니다.
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(my_string: str):
    unique_str = ""
    for index, char in enumerate(my_string):
        if my_string[index] not in unique_str:
            unique_str += my_string[index]

    return unique_str


@prvalue(print_result=True)
def solution001(my_string: str):
    return "".join(dict.fromkeys(my_string))


if __name__ == '__main__':
    assert solution("people") == "peol"
    assert solution("We are the world") == "We arthwold"

    assert solution001("people") == "peol"
    assert solution001("We are the world") == "We arthwold"

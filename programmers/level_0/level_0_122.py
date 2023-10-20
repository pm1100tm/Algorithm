"""
A로 B 만들기

문자열 before와 after가 매개변수로 주어질 때,
before의 순서를 바꾸어 after를 만들 수 있으면 1을,
만들 수 없으면 0을 return 하도록 solution 함수를 완성해보세요.

0 < before의 길이 == after의 길이 < 1,000
before와 after는 모두 소문자로 이루어져 있습니다.

"olleh"	"hello"	1
"allpe"	"apple"	0
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(before, after):
    a = sorted(before)
    b = sorted(after)
    return int(a == b)


@prvalue(print_result=True)
def solution001(before, after):
    len_a, len_b = len(before), len(after)
    if len_a != len_b:
        return 0

    str_list_a = sorted(before)
    str_list_b = sorted(after)

    for index, v in enumerate(str_list_a):
        if str_list_b[index] != v:
            return 0

    return 1


if __name__ == '__main__':
    assert solution("olleh", "hello") == 1
    assert solution("allpe", "apple") == 0

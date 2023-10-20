"""
숨어있는 숫자의 덧셈 (2)

문자열 my_string이 매개변수로 주어집니다.
my_string은 소문자, 대문자, 자연수로만 구성되어있습니다.
my_string안의 자연수들의 합을 return하도록 solution 함수를 완성해주세요.

1 ≤ my_string의 길이 ≤ 1,000
1 ≤ my_string 안의 자연수 ≤ 1000
연속된 수는 하나의 숫자로 간주합니다.
000123과 같이 0이 선행하는 경우는 없습니다.
문자열에 자연수가 없는 경우 0을 return 해주세요.

"aAb1B2cC34oOp"	37
"1a2b3c4d123Z"	133
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(my_string: str):
    answer = 0
    num = 0
    for char in my_string:
        if char.isdigit():
            num = num * 10 + int(char)
        else:
            answer += num
            num = 0

    if num:
        answer += num

    return answer


@prvalue(print_result=True)
def solution001(my_string: str):
    num_list: list[int] = []
    sequential_number_str = ""

    for char in my_string:
        if not char.isdigit():
            if sequential_number_str:
                num_list.append(int(sequential_number_str))
                sequential_number_str = ""
            continue

        sequential_number_str += char

    if sequential_number_str:
        num_list.append(int(sequential_number_str))

    return sum(num_list)


@prvalue(print_result=True)
def solution002(my_string: str):
    n_string = ''.join([char if char.isdigit() else " " for char in my_string])
    return sum(int(char) for char in n_string.split())


@prvalue(print_result=True)
def solution003(my_string: str):
    import re

    r: list[str] = re.findall(r'[0-9]+', my_string)
    return sum(map(int, r))


if __name__ == '__main__':
    solution("aAb1B2cC34oOp")
    solution("1a2b3c4d123Z")
    solution("asfljijokjaflkdd")
    solution("123a123a123a123a")
    solution("AAA1")

    solution001("aAb1B2cC34oOp")
    solution001("1a2b3c4d123Z")
    solution001("asfljijokjaflkdd")
    solution001("123a123a123a123a")
    solution001("AAA1")

    solution002("aAb1B2cC34oOp")
    solution002("1a2b3c4d123Z")
    solution002("asfljijokjaflkdd")
    solution002("123a123a123a123a")
    solution002("AAA1")

"""
세로 읽기

문자열 my_string과 두 정수 m, c가 주어집니다.
my_string을 한 줄에 m 글자씩 가로로 적었을 때 왼쪽부터 세로로
c번째 열에 적힌 글자들을 문자열로 return 하는 solution 함수를 작성해 주세요.

my_string은 영소문자로 이루어져 있습니다.
1 ≤ m ≤ my_string의 길이 ≤ 1,000
m은 my_string 길이의 약수로만 주어집니다.
1 ≤ c ≤ m

"ihrhbakrfpndopljhygc"	4	2	"happy"
"programmers"	1	1	"programmers"
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(my_string, m: int, c: int):
    if m == 1:
        return my_string

    str_list = []
    loop = len(my_string) // m
    for i in range(loop):
        if i == 0:
            str_list.append(my_string[i:m])
        else:
            s = i * m
            e = s + m
            str_list.append(my_string[s:e])

    ret = ""
    for t in str_list:
        ret += t[c-1]

    return ret


@prvalue(print_result=True)
def solution001(my_string, m: int, c: int):
    return my_string[c-1::m]


@prvalue(print_result=True)
def solution002(my_string, m: int, c: int):
    from functools import reduce

    return reduce(lambda x, y: x[c-1::m], my_string)


if __name__ == '__main__':
    # assert solution("ihrhbakrfpndopljhygc", 4, 2) == "happy"
    # assert solution("programmers", 1, 1) == "programmers"
    # assert solution001("ihrhbakrfpndopljhygc", 4, 2) == "happy"
    # assert solution001("programmers", 1, 1) == "programmers"
    solution002("ihrhbakrfpndopljhygc", 4, 2)
    solution002("programmers", 1, 1)

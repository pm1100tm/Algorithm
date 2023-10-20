"""
문자열 뒤집기

문자열 my_string과 정수 s, e가 매개변수로 주어질 때,
my_string에서 인덱스 s부터 인덱스 e까지를 뒤집은 문자열을 return 하는 solution 함수를 작성해 주세요.

my_string은 숫자와 알파벳으로만 이루어져 있습니다.
1 ≤ my_string의 길이 ≤ 1,000
0 ≤ s ≤ e < my_string의 길이

"Progra21Sremm3"	6	12	"ProgrammerS123"
"Stanley1yelnatS"	4	10	"Stanley1yelnatS"
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(my_string, s, e):
    a = my_string[:s]
    b = my_string[e+1:]
    c = my_string[s:e + 1]
    c = c[::-1]

    return a + c + b


if __name__ == '__main__':
    assert solution("Progra21Sremm3", 6, 12) == "ProgrammerS123"
    assert solution("Stanley1yelnatS", 4, 10) == "Stanley1yelnatS"

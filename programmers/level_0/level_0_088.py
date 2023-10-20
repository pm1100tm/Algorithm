"""
문자열 정렬하기 (1)

문자열 my_string이 매개변수로 주어질 때,
my_string 안에 있는 숫자만 골라 오름차순 정렬한 리스트를 return 하도록 solution 함수를 작성해보세요.

1 ≤ my_string의 길이 ≤ 100
my_string에는 숫자가 한 개 이상 포함되어 있습니다.
my_string은 영어 소문자 또는 0부터 9까지의 숫자로 이루어져 있습니다. - - -

"hi12392"	[1, 2, 2, 3, 9]
"p2o4i8gj2"	[2, 2, 4, 8]
"abcde0"	[0]
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(my_string: str):
    return sorted([int(s) for s in my_string if s.isdigit()])


@prvalue(print_result=True)
def solution001(my_string: str):
    return sorted(map(int, filter(lambda x: x.isdigit(), my_string)))


if __name__ == '__main__':
    assert solution("hi12392") == [1, 2, 2, 3, 9]
    assert solution("p2o4i8gj2") == [2, 2, 4, 8]
    assert solution("abcde0") == [0]

    assert solution001("hi12392") == [1, 2, 2, 3, 9]
    assert solution001("p2o4i8gj2") == [2, 2, 4, 8]
    assert solution001("abcde0") == [0]

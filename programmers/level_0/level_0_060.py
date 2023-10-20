"""
문자열 바꿔서 찾기

문자 "A"와 "B"로 이루어진 문자열 myString과 pat가 주어집니다.
myString의 "A"를 "B"로, "B"를 "A"로 바꾼 문자열의 연속하는 부분 문자열 중 pat이
있으면 1을 아니면 0을 return 하는 solution 함수를 완성하세요.

1 ≤ myString의 길이 ≤ 100
1 ≤ pat의 길이 ≤ 10
myString과 pat는 문자 "A"와 "B"로만 이루어진 문자열입니다.

"ABBAA"	"AABB"	1
"ABAB"	"ABAB"	0
"""
from utils import prvalue


@prvalue()
def solution(my_string: str, pat: str):
    reversed_str = "".join(map(lambda x: 'B' if x == 'A' else 'A', my_string))
    return int(pat in reversed_str)


@prvalue()
def solution001(my_string: str, pat: str):
    reversed_pat = "".join(map(lambda x: 'B' if x == 'A' else 'A', pat))
    return int(reversed_pat in my_string)


@prvalue()
def solution002():
    pass


if __name__ == '__main__':
    assert solution("ABBAA", "AABB") == 1
    assert solution("ABAB", "ABAB") == 0
    assert solution001("ABBAA", "AABB") == 1
    assert solution001("ABAB", "ABAB") == 0

    # Since the length limit of pat param is mush lower,
    # this quiz is much faster to check by using pat param.

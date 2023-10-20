"""
문자열 섞기

길이가 같은 두 문자열 str1과 str2가 주어집니다.
두 문자열의 각 문자가 앞에서부터 서로 번갈아가면서 한 번씩 등장하는 문자열을 만들어
return 하는 solution 함수를 완성해 주세요.

1 ≤ str1의 길이 = str2의 길이 ≤ 10
str1과 str2는 알파벳 소문자로 이루어진 문자열입니다.
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(str1, str2):
    return "".join(list(map(lambda x: x[0] + x[1], zip(str1, str2))))


@prvalue(print_result=True)
def solution001(str1, str2):
    answer = ""
    for s1, s2 in zip(str1, str2):
        answer += s1 + s2

    return answer


if __name__ == '__main__':
    assert solution("aaaaa", "bbbbb") == "ababababab"
    assert solution001("aaaaa", "bbbbb") == "ababababab"

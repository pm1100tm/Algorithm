"""
문자열 묶기

문자열 배열 strArr이 주어집니다.
strArr의 원소들을 길이가 같은 문자열들끼리 그룹으로 묶었을 때 가장 개수가 많은 그룹의 크기를
return 하는 solution 함수를 완성해 주세요.

1 ≤ strArr의 길이 ≤ 100,000
1 ≤ strArr의 원소의 길이 ≤ 30
strArr의 원소들은 알파벳 소문자로 이루어진 문자열입니다.

["a","bc","d","efg","hi"] 2
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(str_arr: list[str]):
    grouped_strings = {}
    for s in str_arr:
        length = len(s)
        if length not in grouped_strings:
            grouped_strings[length] = 1
        else:
            grouped_strings[length] += 1

    return max(grouped_strings.values())


@prvalue(print_result=True)
def solution001(str_arr: list[str]):
    d = {}
    for s in str_arr:
        k = len(s)
        d[k] = d.get(k, 0) + 1

    return max(d.values())


if __name__ == '__main__':
    solution(["a","bc","d","efg","hi"])
    solution001(["a","bc","d","efg","hi"])

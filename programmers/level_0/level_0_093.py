"""
ad 제거하기

문자열 배열 strArr가 주어집니다.
배열 내의 문자열 중 "ad"라는 부분 문자열을 포함하고 있는
모든 문자열을 제거하고 남은 문자열을 순서를 유지하여 배열로 return 하는 solution 함수를 완성해 주세요.

1 ≤ strArr의 길이 ≤ 1,000
1 ≤ strArr의 원소의 길이 ≤ 20
strArr의 원소는 알파벳 소문자로 이루어진 문자열입니다.

["and","notad","abcd"]	["and","abcd"]
["there","are","no","a","ds"]	["there","are","no","a","ds"]
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(str_array: list[str]):
    return [_str for _str in str_array if not _str.count("ad")]


@prvalue(print_result=True)
def solution001(str_array: list[str]):
    return [_str for _str in str_array if "ad" not in _str]


if __name__ == '__main__':
    solution(["and","notad","abcd"])
    solution(["there","are","no","a","ds"])

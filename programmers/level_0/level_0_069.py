"""
배열에서 문자열 대소문자 변환하기

문자열 배열 strArr가 주어집니다.
모든 원소가 알파벳으로만 이루어져 있을 때, 배열에서 홀수번째 인덱스의 문자열은 모든 문자를 대문자로,
짝수번째 인덱스의 문자열은 모든 문자를 소문자로 바꿔서 반환하는 solution 함수를 완성해 주세요.

1 ≤ strArr ≤ 20
1 ≤ strArr의 원소의 길이 ≤ 20
strArr의 원소는 알파벳으로 이루어진 문자열 입니다.

["AAA","BBB","CCC","DDD"]	["aaa","BBB","ccc","DDD"]
["aBc","AbC"]	["abc","ABC"]
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(str_array: list[str]) -> list[str]:
    return [
        s.lower() if index % 2 == 0 else s.upper()
        for index, s in enumerate(str_array)
    ]


if __name__ == '__main__':
    solution(["AAA","BBB","CCC","DDD"])
    solution(["aBc","AbC"])

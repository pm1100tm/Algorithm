"""
모음 제거

영어에선 a, e, i, o, u 다섯 가지 알파벳을 모음으로 분류합니다.
문자열 my_string이 매개변수로 주어질 때 모음을 제거한 문자열을 return하도록 solution 함수를 완성해주세요.

my_string은 소문자와 공백으로 이루어져 있습니다.
1 ≤ my_string의 길이 ≤ 1,000
"""
import re
from utils import prvalue


@prvalue(print_time=True)
def solution(my_string: str) -> str:
    pattern = r"[$aeiou]"
    answer = re.sub(pattern, "", my_string)

    return answer


@prvalue(print_time=True)
def solution001(my_string: str) -> str:
    return "".join([i for i in my_string if not(i in "aeiou")])


if __name__ == '__main__':
    assert solution("bus") == "bs"
    assert solution("nice to meet you") == "nc t mt y"

    assert solution001("bus") == "bs"
    assert solution001("nice to meet you") == "nc t mt y"

    # 왠만하면 리스트 컴프리헨션이 가장 빠르다

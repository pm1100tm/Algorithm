"""
대문자와 소문자

문자열 my_string이 매개변수로 주어질 때,
대문자는 소문자로 소문자는 대문자로 변환한 문자열을 return하도록 solution 함수를 완성해주세요.

1 ≤ my_string의 길이 ≤ 1,000
my_string은 영어 대문자와 소문자로만 구성되어 있습니다.

"cccCCC"	"CCCccc"
"abCdEfghIJ"	"ABcDeFGHij"
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(my_string: str) -> str:
    answer: str = ""
    for char in my_string:
        answer += char.upper() if char.islower() else char.lower()

    return answer


@prvalue(print_result=True)
def solution001(my_string: str) -> str:
    return my_string.swapcase()


if __name__ == '__main__':
    assert solution("cccCCC") == "CCCccc"
    assert solution("abCdEfghIJ") == "ABcDeFGHij"

    assert solution001("cccCCC") == "CCCccc"
    assert solution001("abCdEfghIJ") == "ABcDeFGHij"

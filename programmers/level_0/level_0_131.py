"""
세 개의 구분자

임의의 문자열이 주어졌을 때 문자 "a", "b", "c"를 구분자로 사용해 문자열을 나누고자 합니다.
예를 들어 주어진 문자열이 "baconlettucetomato"라면 나눠진 문자열 목록은 ["onlettu", "etom", "to"] 가 됩니다.
문자열 myStr이 주어졌을 때 위 예시와 같이 "a", "b", "c"를 사용해 나눠진 문자열을 순서대로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.
단, 두 구분자 사이에 다른 문자가 없을 경우에는 아무것도 저장하지 않으며, return할 배열이 빈 배열이라면 ["EMPTY"]를 return 합니다.

1 ≤ myStr의 길이 ≤ 1,000,000
myStr은 알파벳 소문자로 이루어진 문자열 입니다.

"baconlettucetomato"	["onlettu", "etom", "to"]
"abcd"	["d"]
"cabab"	["EMPTY"]
"""
from utils import prvalue


@prvalue(print_time=True)
def solution(my_str: str):
    remove_char_list = ["a", "b", "c"]
    removed_str = my_str
    for x in remove_char_list:
        removed_str = ",".join(removed_str.split(x))

    answer = [chars for chars in removed_str.split(",") if chars]
    if not answer:
        return ["EMPTY"]

    return answer


@prvalue(print_time=True)
def solution001(my_str: str):
    import re
    answer = [chars for chars in re.split("a|b|c", my_str) if chars]
    return answer if answer else ["EMPTY"]


@prvalue(print_result=True)
def solution002(my_str: str):
    REP_CHAR = " "
    replaced_str = (
        my_str
        .replace("a", REP_CHAR)
        .replace("b", REP_CHAR)
        .replace("c", REP_CHAR)
    )

    answer = [chars for chars in replaced_str.split() if chars]

    return answer if answer else ["EMPTY"]


if __name__ == '__main__':
    assert solution("baconlettucetomato") == ["onlettu", "etom", "to"]
    assert solution("abcd") == ["d"]
    assert solution("cabab") == ["EMPTY"]
    assert solution001("baconlettucetomato") == ["onlettu", "etom", "to"]
    assert solution001("abcd") == ["d"]
    assert solution001("cabab") == ["EMPTY"]
    assert solution002("baconlettucetomato") == ["onlettu", "etom", "to"]
    assert solution002("abcd") == ["d"]
    assert solution002("cabab") == ["EMPTY"]

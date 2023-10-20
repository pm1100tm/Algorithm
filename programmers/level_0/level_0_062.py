"""
접미사인지 확인하기

어떤 문자열에 대해서 접미사는 특정 인덱스부터 시작하는 문자열을 의미합니다.
예를 들어, "banana"의 모든 접미사는 "banana", "anana", "nana", "ana", "na", "a"입니다.
문자열 my_string과 is_suffix가 주어질 때, is_suffix가 my_string의 접미사라면 1을, 아니면 0을
return 하는 solution 함수를 작성해 주세요.

1 ≤ my_string의 길이 ≤ 100
1 ≤ is_suffix의 길이 ≤ 100
my_string과 is_suffix는 영소문자로만 이루어져 있습니다.
"""
from utils import prvalue


@prvalue()
def solution(my_string: str, is_suffix: str) -> int:
    return my_string[::-1].startswith(is_suffix[::-1])


@prvalue()
def solution001(my_string: str, is_suffix: str) -> int:
    len_str = len(my_string)
    len_suf = len(is_suffix)
    if len_str < len_suf:
        return 0

    if my_string[-len_suf:] != is_suffix:
        return 0

    return 1


@prvalue()
def solution002():
    pass


if __name__ == '__main__':
    assert solution("banana", "a") == 1
    assert solution("banana", "na") == 1
    assert solution("banana", "ana") == 1
    assert solution("banana", "nana") == 1
    assert solution("banana", "anana") == 1
    assert solution("banana", "banana") == 1
    assert solution("banana", "abanana") == 0
    assert solution("banana", "bbanana") == 0
    assert solution("banana", "nan") == 0
    assert solution("banana", "wxyz") == 0

    assert solution001("banana", "a") == 1
    assert solution001("banana", "na") == 1
    assert solution001("banana", "ana") == 1
    assert solution001("banana", "nana") == 1
    assert solution001("banana", "anana") == 1
    assert solution001("banana", "banana") == 1
    assert solution001("banana", "abanana") == 0
    assert solution001("banana", "bbanana") == 0
    assert solution001("banana", "nan") == 0
    assert solution001("banana", "wxyz") == 0

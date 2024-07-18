"""뉴스 클러스터링
https://school.programmers.co.kr/learn/courses/30/lessons/17677
"""
from utils import prvalue

import re
from collections import Counter


def check_only_eng_characters(str_: str) -> bool:
    """영어 소문자, 대문자만 들어있는지 체크하는 정규식
    """
    pattern = r'^[a-zA-Z]+$'
    return bool(re.search(pattern, str_))


def slice_two_char_using_regex_and_lower(s: str) -> list[str]:
    return [
        s[i:i + 2].upper() for i in range(len(s) - 1)
        if check_only_eng_characters(s[i:i + 2])
    ]


@prvalue(print_result=True)
def solution(str1: str, str2: str) -> int:
    a_list = slice_two_char_using_regex_and_lower(str1)
    b_list = slice_two_char_using_regex_and_lower(str2)

    a_counter = Counter(a_list)
    b_counter = Counter(b_list)

    iters_list = list((a_counter & b_counter).elements())
    union_list = list((a_counter | b_counter).elements())

    a_len = len(iters_list)
    b_len = len(union_list)

    if not b_len:
        return 65536

    return int((a_len / b_len) * 65536)


@prvalue(print_result=True)
def solution2(str1: str, str2: str) -> int:
    def make_multiset(s: str) -> list[str]:
        return [s[i:i + 2].lower() for i in range(len(s) - 1) if s[i:i+2].isalpha()]

    multiset1 = make_multiset(str1)
    multiset2 = make_multiset(str2)

    counter1 = Counter(multiset1)
    counter2 = Counter(multiset2)

    inter_ = sum((counter1 & counter2).values())
    union_ = sum((counter1 | counter2).values())

    if not union_:
        return 65536

    return int((inter_ / union_) * 65536)


if __name__ == '__main__':
    assert solution('FRANCE', 'french') == 16384
    assert solution('handshake', 'shake hands') == 65536
    assert solution('aa1+aa2', 'AAAA12') == 43690
    assert solution('E=M*C^2', 'e=m*c^2') == 65536

    assert solution2('FRANCE', 'french') == 16384
    assert solution2('handshake', 'shake hands') == 65536
    assert solution2('aa1+aa2', 'AAAA12') == 43690
    assert solution2('E=M*C^2', 'e=m*c^2') == 65536

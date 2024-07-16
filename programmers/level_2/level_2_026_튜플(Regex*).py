"""튜플
https://school.programmers.co.kr/learn/courses/30/lessons/64065
"""
from utils import prvalue

import re
from collections import Counter


@prvalue(print_result=True)
def solution(s: str) -> list[int]:
    answer = {}
    _s = s.replace('{{', '').replace('}}', '').split('},')
    _s.sort(key=len)
    for char_seq in _s:
        for char in char_seq.replace('{', '').split(','):
            answer[int(char)] = 0

    return [k for k in answer.keys()]


@prvalue(print_result=True)
def solution2(s: str) -> list[int]:
    tuple_nums = Counter(re.findall('\d+', s))
    return [
        int(k) for k, _ in sorted(tuple_nums.items(), key=lambda x: x[1], reverse=True)
    ]


if __name__ == '__main__':
    assert solution("{{2},{2,1},{2,1,3},{2,1,3,4}}") == [2, 1, 3, 4]
    assert solution("{{1,2,3},{2,1},{1,2,4,3},{2}}") == [2, 1, 3, 4]
    assert solution("{{20,111},{111}}") == [111, 20]
    assert solution("{{123}}") == [123]
    assert solution("{{4,2,3},{3},{2,3,4,1},{2,3}}") == [3, 2, 4, 1]

    assert solution2("{{2},{2,1},{2,1,3},{2,1,3,4}}") == [2, 1, 3, 4]
    assert solution2("{{1,2,3},{2,1},{1,2,4,3},{2}}") == [2, 1, 3, 4]
    assert solution2("{{20,111},{111}}") == [111, 20]
    assert solution2("{{123}}") == [123]
    assert solution2("{{4,2,3},{3},{2,3,4,1},{2,3}}") == [3, 2, 4, 1]

"""
머쓱이는 태어난 지 6개월 된 조카를 돌보고 있습니다. 조카는 아직 "aya", "ye", "woo", "ma"
네 가지 발음을 최대 한 번씩 사용해 조합한(이어 붙인) 발음밖에 하지 못합니다. 문자열 배열 babbling이
매개변수로 주어질 때, 머쓱이의 조카가 발음할 수 있는 단어의 개수를 return하도록 solution 함수를
완성해주세요.

제한사항
- babbling의 각 문자열에서 "aya", "ye", "woo", "ma"는 각각 최대 한 번씩만 등장합니다.
  - 즉, 각 문자열의 가능한 모든 부분 문자열 중에서 "aya", "ye", "woo", "ma"가 한 번씩만 등장합니다.
- 문자열은 알파벳 소문자로만 이루어져 있습니다.
"""
from utils import prvalue


@prvalue(print_result=False)
def solution(babbling):
    str_list = babbling[:]
    words = ["aya", "ye", "woo", "ma"]

    count = 0
    for s in str_list:
        for w in words:
            s = s.replace(w, ' ')
        if not s.replace(' ', ''):
            count += 1

    return count


import re


def solution2(babbling: list[str]):
    regex = re.compile('^(aya|ye|woo|ma)+$')
    count = 0
    for b in babbling:
        if regex.match(b):
            count += 1
    return count


if __name__ == '__main__':
    """
    위의 코드는 yemama 와 같이 같은 단어가 중복될 때는 유효하지 못하다.
    그러나 'babbling의 각 문자열에서 "aya", "ye", "woo", "ma"는 각각 최대 한 번씩만 등장' 한다는
    제안사항에 의해서 해당 케이스는 테스트 케이스로 넣지 않는다.
    """
    assert solution(["aya", "yee", "u", "maa", "wyeoo"]) == 1
    assert solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]) == 3
    assert solution(["aye"]) == 0

    assert solution2(["aya", "yee", "u", "maa", "wyeoo"]) == 1
    assert solution2(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]) == 3
    assert solution2(["aye"]) == 0

    # assert solution(['yemama']) == 0

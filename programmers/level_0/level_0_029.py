"""
배열의 유사도

두 배열이 얼마나 유사한지 확인해보려고 합니다.
문자열 배열 s1과 s2가 주어질 때 같은 원소의 개수를 return하도록 solution 함수를 완성해주세요.

1 ≤ s1, s2의 길이 ≤ 100
1 ≤ s1, s2의 원소의 길이 ≤ 10
s1과 s2의 원소는 알파벳 소문자로만 이루어져 있습니다
s1과 s2는 각각 중복된 원소를 갖지 않습니다.
"""
from utils import prvalue


@prvalue()
def solution(s1: list[str], s2: list[str]) -> int:
    unique_num: int = len(set(s1 + s2))
    answer: int = (len(s1) + len(s2)) - unique_num

    return answer


def solution001(s1: list[str], s2: list[str]) -> int:
    set1, set2 = set(s1), set(s2)
    answer1: int = len(set1.intersection(set2))
    answer2: int = len(set1 & set2)
    assert answer1 == answer2

    return answer1


if __name__ == '__main__':
    assert solution(["a", "b", "c"], ["com", "b", "d", "p", "c"]) == 2
    assert solution(["n", "omg"], ["m", "dot"]) == 0

    assert solution001(["a", "b", "c"], ["com", "b", "d", "p", "c"]) == 2
    assert solution001(["n", "omg"], ["m", "dot"]) == 0

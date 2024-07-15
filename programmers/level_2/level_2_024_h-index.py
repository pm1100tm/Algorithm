"""H-Index
https://school.programmers.co.kr/learn/courses/30/lessons/42747
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(citations: list[int]) -> int:
    h_index = 0
    n = len(citations)
    for i, v in enumerate(sorted(citations)):
        # i: 논문의 수, v: 인용된 수, h: i번 이상 인용된 논문의 수
        h = n - i
        if v >= h:
            h_index = h
            break

    return h_index


@prvalue(print_result=True)
def solution2(citations: list[int]) -> int:
    sorted_citations = sorted(citations, reverse=True)
    h_index = 0
    for i, citation in enumerate(sorted_citations):
        if citation >= i + 1:
            h_index = i + 1
        else:
            break

    return h_index


if __name__ == '__main__':
    solution([3, 0, 6, 1, 5])

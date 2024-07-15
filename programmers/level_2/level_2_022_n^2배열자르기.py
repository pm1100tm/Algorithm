"""n^2 배열 자르기
https://school.programmers.co.kr/learn/courses/30/lessons/87390
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(n: int, left: int, right: int) -> list[int]:
    answer = []
    for i in range(left, right + 1):
        row = i // n
        col = i % n
        answer.append(max(row, col) + 1)

    return answer


if __name__ == '__main__':
    assert solution(3, 2, 5) == [3,2,2,3]
    assert solution(4, 7, 14) == [4,3,3,3,4,4,4,4]

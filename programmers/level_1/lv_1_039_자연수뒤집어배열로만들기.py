"""자연수 뒤집어 배열로 만들기
https://school.programmers.co.kr/learn/courses/30/lessons/12932
"""


def solution(n: int) -> list[int]:
    return [int(_n) for _n in str(n)[::-1]]


if __name__ == '__main__':
    assert solution(12345) == [5,4,3,2,1]

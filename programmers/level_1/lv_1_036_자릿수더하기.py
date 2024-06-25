"""자릿수 더하기
https://school.programmers.co.kr/learn/courses/30/lessons/12931
"""


def solution(n: int) -> int:
    answer = sum(map(int, str(n)))
    return answer


def solution2(n: int) -> int:
    answer = sum([int(num) for num in str(n)])
    return answer


def solution3(n: int) -> int:
    if n < 10:
        return n

    quo, rem = divmod(n, 10)

    return rem + solution(quo)


if __name__ == '__main__':
    assert solution(123) == 6
    assert solution(987) == 24
    assert solution2(123) == 6
    assert solution2(987) == 24
    assert solution3(123) == 6
    assert solution3(987) == 24

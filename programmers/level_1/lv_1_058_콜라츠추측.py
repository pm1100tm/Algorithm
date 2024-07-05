"""콜라츠 추측
https://school.programmers.co.kr/learn/courses/30/lessons/12943
- DFS(Depth Fist Search)
"""


def solution(num: int) -> int:
    count = 0
    while num != 1:
        num = num / 2 if num % 2 == 0 else num * 3 + 1
        count += 1

        if count > 500:
            return -1

        elif num == 1:
            break

    return count


if __name__ == '__main__':
    assert solution(6) == 8
    assert solution(16) == 4
    assert solution(626331) == -1

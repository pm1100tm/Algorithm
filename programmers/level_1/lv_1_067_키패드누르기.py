"""키패드 누르기
https://school.programmers.co.kr/learn/courses/30/lessons/67256
"""


def solution(numbers: list[int], hand: str) -> str:
    position = {
        # left
        1: (0, 0),
        4: (1, 0),
        7: (2, 0),

        # right
        3: (0, 2),
        6: (1, 2),
        9: (2, 2),

        # middle
        2: (0, 1),
        5: (1, 1),
        8: (2, 1),
        0: (3, 1)
    }

    lp = (3, 0)
    rp = (3, 2)

    answer = ''

    for n in numbers:

        if n == 1 or n == 4 or n == 7:
            answer += 'L'
            lp = position[n]
            continue

        if n == 3 or n == 6 or n == 9:
            answer += 'R'
            rp = position[n]
            continue

        from_l = abs(position[n][0] - lp[0]) + abs(position[n][1] - lp[1])
        from_r = abs(position[n][0] - rp[0]) + abs(position[n][1] - rp[1])

        if from_l == from_r:
            if hand == 'right':
                answer += 'R'
                rp = position[n]
                continue

            answer += 'L'
            lp = position[n]
            continue

        if from_l > from_r:
            answer += 'R'
            rp = position[n]
            continue
        else:
            answer += 'L'
            lp = position[n]
            continue

    return answer


if __name__ == '__main__':
    assert solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right') == 'LRLLLRLLRRL'
    assert solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left') == 'LRLLRRLLLRR'
    assert solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 'right') == "LLRLLRLLRL"

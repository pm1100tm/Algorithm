"""크레인 인형뽑기 게임
https://school.programmers.co.kr/learn/courses/30/lessons/64061
"""


def solution(board: list[list[int]], moves: list[int]):
    count = 0
    answer = []

    for m in moves:

        for b in board:

            if b[m - 1] != 0:
                temp = b[m - 1]

                if not answer:
                    b[m - 1] = 0
                    answer.append(temp)
                    break

                if answer[-1] != temp:
                    b[m - 1] = 0
                    answer.append(temp)
                    break

                else:
                    count += 2
                    b[m - 1] = 0
                    answer.pop()
                    break

    return count


if __name__ == '__main__':
    assert solution(
        [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 3],
            [0, 2, 5, 0, 1],
            [4, 2, 4, 4, 2],
            [3, 5, 1, 3, 1],
        ],
        [1, 5, 3, 5, 1, 2, 1, 4],
    ) == 4

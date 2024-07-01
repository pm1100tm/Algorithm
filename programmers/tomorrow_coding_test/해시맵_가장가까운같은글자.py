"""가장 가까운 같은 글자
https://school.programmers.co.kr/tryouts/85914/challenges?language=python3
"""


def solution(s: str):
    last_seen = {}
    answer = []

    for i, char in enumerate(s):
        if char not in last_seen:
            answer.append(-1)
        else:
            answer.append(i - last_seen[char])

        last_seen[char] = i

    return answer


if __name__ == '__main__':
    solution("banana") # [-1, -1, -1, 2, 2, 2]
    solution("foobar") # [-1, -1, 1, -1, -1, -1]

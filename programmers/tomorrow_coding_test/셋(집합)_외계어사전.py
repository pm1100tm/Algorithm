"""외계어 사전
https://school.programmers.co.kr/tryouts/85920/challenges?language=python3
"""


def solution(spell, dic):
    answer = 2
    chars = ''.join(sorted(set(spell)))
    for d in dic:
        if ''.join(sorted(d)) == chars:
            answer = 1
            break

    return answer


if __name__ == '__main__':
    assert solution(["p", "o", "s"], ["sod", "eocd", "qixm", "adio", "soo"]) == 2
    assert solution(["z", "d", "x"]	, ["def", "dww", "dzx", "loveaw"]) == 1
    assert solution(["s", "o", "m", "d"], ["moos", "dzx", "smm", "sunmmo", "som"]) == 2

"""성격 유형 검사하기
https://school.programmers.co.kr/tryouts/85913/challenges?language=python3
"""
from collections import defaultdict


def solution(survey: list[str], choices: list[int]):
    score = {
        1: 3,
        2: 2,
        3: 1,
        4: 0,
        5: 1,
        6: 2,
        7: 3,
    }

    p_map = defaultdict(int)
    for (p1, p2), choice in zip(survey, choices):
        if choice < 4:
            p_map[p1] += score[choice]
        else:
            p_map[p2] += score[choice]

    answer = ''
    for (p1, p2) in ['RT', 'CF', 'JM', 'AN']:
        if p_map[p1] == p_map[p2]:
            answer += min(p1, p2)
            continue
        answer += p1 if p_map[p1] > p_map[p2] else p2

    return answer


if __name__ == '__main__':
    assert solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]) == 'TCMA'
    assert solution(["TR", "RT", "TR"], [7, 1, 3]) == 'RCJA'

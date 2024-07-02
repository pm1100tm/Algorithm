"""완주하지 못한 선수
https://school.programmers.co.kr/tryouts/85916/challenges?language=python3
"""


def solution(participant: list[str], completion: list[str]) -> str:
    participant.sort()
    completion.sort()

    answer = ''
    for v1, v2 in zip(participant, completion):
        if v1 != v2:
            answer = v1
            break

    if not answer:
        answer = participant[-1]

    return answer


def solution2(participant: list[str], completion: list[str]) -> str:
    p_dict = {}
    for p in participant:
        if p not in p_dict:
            p_dict[p] = 1
        else:
            p_dict[p] += 1

    for c in completion:
        if p_dict[c] == 1:
            del p_dict[c]
        else:
            p_dict[c] -= 1

    return next(iter(p_dict.keys()))


if __name__ == '__main__':
    assert solution(["leo", "kiki", "eden"], ["eden", "kiki"]) == 'leo'
    assert (
        solution(
            ["mislav", "stanko", "mislav", "ana"],
            ["stanko", "ana", "mislav"]),
    ) == 'mislav'

    assert solution2(["leo", "kiki", "eden"], ["eden", "kiki"]) == 'leo'
    assert (
        solution2(
            ["mislav", "stanko", "mislav", "ana"],
            ["stanko", "ana", "mislav"]),
    ) == 'mislav'

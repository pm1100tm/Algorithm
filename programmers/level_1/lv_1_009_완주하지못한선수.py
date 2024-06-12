from collections import Counter


def solution(participant: list[str], completion: list[str]):
    participant.sort()
    completion.sort()

    for i, c in enumerate(completion):
        if c != participant[i]:
            return participant[i]

    return participant[-1]


def solution2(participant: list[str], completion: list[str]):
    pc = Counter(participant)
    cc = Counter(completion)

    return list((pc - cc).keys())[-1]


if __name__ == '__main__':
    assert solution(['leo', 'kiki', 'eden'], ["eden", "kiki"]) == 'leo'
    assert solution(
        ['marina', 'josipa', 'nikola', 'vinko', 'filipa'],
        ["josipa", "filipa", "marina", "nikola"],
    ) == 'vinko'
    assert solution(
        ['mislav', 'stanko', 'mislav', 'ana'],
        ["stanko", "ana", "mislav"],
    ) == 'mislav'

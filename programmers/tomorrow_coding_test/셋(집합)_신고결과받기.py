"""신고 결과 받기
https://school.programmers.co.kr/tryouts/85925/challenges?language=python3
"""
from collections import defaultdict


def solution(id_list: list[str], report: list[str], k: int) -> list[int]:
    user_dic = {user_id: set() for user_id in id_list}
    reported_count = defaultdict(int)
    for report_desc in set(report):
        user_id, reported_user_id = report_desc.split(' ')
        reported_count[reported_user_id] += 1
        user_dic[user_id].add(reported_user_id)

    answer = [
        len([u for u in report_user_list if reported_count.get(u) >= k])
        for v, report_user_list in user_dic.items()
    ]

    return answer


if __name__ == '__main__':
    assert solution(
        ["muzi", "frodo", "apeach", "neo"],
        ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
        2,
    ) == [2,1,1,0]
    assert solution(
        ["con", "ryan"],
        ["ryan con", "ryan con", "ryan con", "ryan con"],
        3,
    ) == [0, 0]

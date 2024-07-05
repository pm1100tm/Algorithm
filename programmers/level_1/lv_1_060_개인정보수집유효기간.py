"""개인정보 수집 유효기간
https://school.programmers.co.kr/learn/courses/30/lessons/150370
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(today: str, terms: list[str], privacies: list[str]) -> list[int]:

    def convert_date_to_days(date_str: str) -> int:
        _y, _m, _d = date_str.split('.')
        return (int(_y) * 12 * 28) + (int(_m) * 28) + int(_d)

    exp_month_by_terms = {}
    for t in terms:
        term, month = t.split()
        exp_month_by_terms[term] = int(month)

    today_days = convert_date_to_days(today)

    expired_privacies_index = []
    for i, p in enumerate(privacies, 1):
        d, term = p.split()
        days = convert_date_to_days(d)
        days += exp_month_by_terms[term] * 28 - 1
        if today_days > days:
            expired_privacies_index.append(i)

    return expired_privacies_index


if __name__ == '__main__':
    assert solution(
        "2022.05.19",
        ["A 6", "B 12", "C 3"],
        ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
    ) == [1, 3]
    assert solution(
        "2020.01.01",
        ["Z 3", "D 5"],
        ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"],
    ) == [1, 4, 5]

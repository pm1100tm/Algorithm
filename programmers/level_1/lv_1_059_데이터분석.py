"""데이터 분석[PCCE 기출 문제]
https://school.programmers.co.kr/learn/courses/30/lessons/250121
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(
    data: list[list[int]], # [code, date, maximum, remain]
    ext: str,
    val_ext: int,
    sort_by: str,
) -> list[list[int]]:
    head = ['code', 'date', 'maximum', 'remain']

    filtered_data = list(filter(lambda x: x[head.index(ext)] < val_ext, data))

    return sorted(filtered_data, key=lambda x: x[head.index(sort_by)])


if __name__ == '__main__':
    assert solution(
        [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]],
        'date',
        20300501,
        'remain',
    ) == [[3,20300401,10,8],[1,20300104,100,80]]

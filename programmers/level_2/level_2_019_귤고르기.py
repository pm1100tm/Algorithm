"""귤고르기
https://school.programmers.co.kr/learn/courses/30/lessons/138476
"""
from utils import prvalue

from collections import defaultdict, Counter


@prvalue(print_result=True)
def solution(k: int, tangerine: list[int]) -> int:
    tangerine_dic = defaultdict(int)
    for t in tangerine:
        tangerine_dic[t] += 1

    tangerine_list = sorted(
        tangerine_dic.items(), key=lambda x: x[1], reverse=True
    )
    tangerine_dic = dict(tangerine_list)

    num = 0
    num_to_purchase = 0
    for v in tangerine_dic.values():
        num += 1
        num_to_purchase += v
        if num_to_purchase >= k:
            break

    return num


@prvalue(print_result=True)
def solution2(k: int, tangerine: list[int]) -> int:
    answer = 0
    selected_tangerine_num = 0
    counter = Counter(tangerine)
    for v in sorted(counter.values(), reverse=True):
        answer += 1
        selected_tangerine_num += v
        if selected_tangerine_num >= k:
            break

    return answer


if __name__ == '__main__':
    assert solution(6, [1, 3, 2, 5, 4, 5, 2, 3]) == 3
    assert solution(4, [1, 3, 2, 5, 4, 5, 2, 3]) == 2
    assert solution(2, [1, 1, 1, 1, 2, 2, 2, 3]) == 1

    assert solution2(6, [1, 3, 2, 5, 4, 5, 2, 3]) == 3
    assert solution2(4, [1, 3, 2, 5, 4, 5, 2, 3]) == 2
    assert solution2(2, [1, 1, 1, 1, 2, 2, 2, 3]) == 1

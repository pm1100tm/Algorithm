"""붕대 감기
https://school.programmers.co.kr/learn/courses/30/lessons/250137
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(bandage: list[int], health: int, attacks: list[list[int]]) -> int:
    """
    채력이 0이하가 되면 바로 끝나야 함
    """
    cur_h = health
    prev_attack_sec, skill_success_times = 0, 0
    success_times, heal, additional_heal = bandage

    for attack in attacks:
        sec, dam = attack
        total_heal = 0
        for i in range(prev_attack_sec, sec - 1):
            skill_success_times += 1
            total_heal += heal
            if skill_success_times >= success_times:
                total_heal += additional_heal
                skill_success_times = 0

        if cur_h + total_heal > health:
            cur_h = health
        else:
            cur_h += total_heal

        prev_attack_sec = sec
        skill_success_times = 0
        cur_h -= dam

        if cur_h <= 0:
            break

    return -1 if cur_h <= 0 else cur_h


if __name__ == '__main__':
    assert solution([5, 1, 5], 30, [[2, 10], [9, 15], [10, 5], [11, 5]]) == 5
    assert solution([3, 2, 7], 20, [[1, 15], [5, 16], [8, 6]]) == -1
    assert solution([4, 2, 7], 20, [[1, 15], [5, 16], [8, 6]]) == -1
    assert solution([1, 1, 1], 5, [[1, 2], [3, 2]]) == 3
    assert solution([3, 1, 7], 100, [[3, 1]]) == 99
    assert solution([3, 1, 7], 100, [[3, 100], [100, 1]]) == -1

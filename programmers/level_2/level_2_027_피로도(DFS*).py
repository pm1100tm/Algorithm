"""피로도
https://school.programmers.co.kr/learn/courses/30/lessons/87946
- Idea
Permutation or DFS
"""
from utils import prvalue

from itertools import permutations


@prvalue(print_result=True)
def solution(k: int, dungeons: list[list[int]]) -> int:
    """
    Using permutation
    """
    answer = 0
    for pem in permutations(dungeons):
        current_fatigue = k
        visited_dungeon = 0

        for min_required_fatigue, consumed_fatigue in pem:
            if current_fatigue >= min_required_fatigue:
                current_fatigue -= consumed_fatigue
                visited_dungeon += 1
            else:
                break

        answer = max(answer, visited_dungeon)
        if answer == len(dungeons):
            break

    return answer


@prvalue(print_result=True)
def solution2(k: int, dungeons: list[list[int]]) -> int:
    """
    Using DFS
    """
    max_visited_dungeon_nums = 0
    visited = [False] * len(dungeons)

    def dfs(fatigue: int, dgs: list[list[int]], vs: list[bool], count: int):
        nonlocal max_visited_dungeon_nums
        max_visited_dungeon_nums = max(max_visited_dungeon_nums, count)

        for i, (min_required_fatigue, consumed_fatigue) in enumerate(dgs):
            if not vs[i] and fatigue >= min_required_fatigue:
                vs[i] = True
                dfs(fatigue - consumed_fatigue, dgs, vs, count + 1)
                vs[i] = False

    dfs(k, dungeons, visited, 0)

    return max_visited_dungeon_nums


if __name__ == '__main__':
    assert solution(80, [[80, 20], [50, 40], [30, 10]]) == 3
    assert solution2(80, [[80, 20], [50, 40], [30, 10]]) == 3

"""로또의 최고 순위와 최저 순위
https://school.programmers.co.kr/tryouts/85904/challenges?language=python3
"""


def solution(lottos, win_nums):
    win_map = {
        1: 6,
        2: 5,
        3: 4,
        4: 3,
        5: 2,
        6: 1,
    }

    nums = set([n for n in lottos if n != 0])

    min_count = len(nums) - len(nums.difference(set(win_nums)))
    max_count = min_count + lottos.count(0)

    return [win_map.get(max_count, 6), win_map.get(min_count, 6)]


if __name__ == '__main__':
    assert solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]) == [3, 5]
    assert solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]) == [1, 6]
    assert solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]) == [1,1]

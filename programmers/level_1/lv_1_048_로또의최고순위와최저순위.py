"""로또의 최고 순위와 최저 순위
https://school.programmers.co.kr/learn/courses/30/lessons/77484
"""


def solution(lottos: list[int], win_nums: list[int]) -> list[int]:
    win = {
        6: 1,
        5: 2,
        4: 3,
        3: 4,
        2: 5,
        1: 6,
    }

    win_assume_count = 0
    remove_zero_nums = []
    for l in lottos:
        if l == 0:
            win_assume_count += 1
        else:
            remove_zero_nums.append(l)

    min_win_count = len(remove_zero_nums) - len(set(remove_zero_nums) - set(win_nums))
    max_win_count = min_win_count + win_assume_count

    return [win.get(max_win_count, 6), win.get(min_win_count, 6)]


def solution2(lottos: list[int], win_nums: list[int]):
    win_map = {
        6: 1,
        5: 2,
        4: 3,
        3: 4,
        2: 5,
        1: 6,
    }

    cnt_ok, cnt_ze = 0, 0
    for num in lottos:
        if num == 0:
            cnt_ze += 1
            continue

        if num in win_nums:
            cnt_ok += 1
            continue

    return [win_map.get(cnt_ok + cnt_ze, 6), win_map.get(cnt_ok, 6)]


if __name__ == '__main__':
    assert solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]) == [3, 5]
    assert solution([0, 0, 0, 0, 0, 0]	, [38, 19, 20, 40, 15, 25]) == [1, 6]
    assert solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]) == [1, 1]
    assert solution([1,2,3,4,5,0], [7,8,9,10,11,12]) == [6, 6]

    assert solution2([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]) == [3, 5]
    assert solution2([0, 0, 0, 0, 0, 0]	, [38, 19, 20, 40, 15, 25]) == [1, 6]
    assert solution2([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]) == [1, 1]
    assert solution2([1,2,3,4,5,0], [7,8,9,10,11,12]) == [6, 6]

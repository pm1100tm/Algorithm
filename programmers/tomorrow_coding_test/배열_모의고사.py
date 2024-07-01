"""모의고사
https://school.programmers.co.kr/tryouts/85909/challenges?language=python3
"""


def count_ok(pattern_list, answer):
    length = len(pattern_list)
    count = 0
    for i, v in enumerate(answer):
        if pattern_list[i % length] == v:
            count += 1

    return count


def solution(answer: list[int]):
    st1_pattern = [1, 2, 3, 4, 5]
    st2_pattern = [2, 1, 2, 3, 2, 4, 2, 5]
    st3_pattern = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    st_map = {}

    for number, pattern in enumerate(
        [st1_pattern, st2_pattern, st3_pattern], 1
    ):
        st_map[number] = count_ok(pattern, answer)

    max_count = max(st_map.values())
    sorted_map = sorted(st_map.items(), key=lambda x: (x[1], x[0]), reverse=True)
    answer = [
        number for number, answer_count in sorted_map
        if answer_count == max_count
    ]
    answer.sort()

    return answer


if __name__ == '__main__':
    assert solution([1,2,3,4,5]) == [1]
    assert solution([1,3,2,4,2]) == [1, 2, 3]

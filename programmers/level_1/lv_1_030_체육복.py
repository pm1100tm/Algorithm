"""체육복
https://school.programmers.co.kr/learn/courses/30/lessons/42862

n - 전체 학생의 수
lost - 체육복을 도난당한 학생들의 번호가 담긴 배열
reserve - 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열
"""


# def solution(n: int, lost: list[int], reserve: list[int]):
#     can_borrow = 0
#     for student_number in lost:
#         if student_number in reserve:
#             reserve.remove(student_number)
#             can_borrow += 1
#             continue
#
#         l = 1 if student_number == 1 else student_number - 1
#         r = n if student_number == n else student_number + 1
#         if l in reserve:
#             can_borrow += 1
#             reserve.remove(l)
#             continue
#         if r in reserve:
#             can_borrow += 1
#             reserve.remove(r)
#             continue
#
#     print(n - (len(lost) - can_borrow))
#     return n - (len(lost) - can_borrow)

from collections import deque


def solution2(n: int, lost: list[int], reserve: list[int]):
    lost_numbers_set = set(lost)
    resv_numbers_set = set(reserve)
    lost_number_list = list(lost_numbers_set - resv_numbers_set)
    resv_number_list = list(resv_numbers_set - lost_numbers_set)
    lost_number_list.sort()
    resv_number_list.sort()

    can_borrow_count = len(lost) - len(lost_number_list)

    studnet_lost_q = deque(lost_number_list)
    studnet_resv_q = deque(resv_number_list)

    for number in lost_number_list:
        l_num, r_num = number - 1, number + 1
        if l_num in studnet_resv_q or r_num in studnet_resv_q:
            studnet_lost_q.popleft()
            studnet_resv_q.popleft()
            can_borrow_count += 1

    answer = n - (len(lost) - can_borrow_count)

    return answer


if __name__ == '__main__':
    assert solution2(9, [1, 2, 4], [4, 8]) == 7
    assert solution2(5, [2, 4], [1, 3, 5]) == 5
    assert solution2(5, [2, 4], [3]) == 4
    assert solution2(3, [3], [1]) == 2
    assert solution2(3, [3], [3]) == 3
    assert solution2(5, [5, 3], [4, 2]) == 5
    assert solution2(5, [1, 2], [2, 3]) == 4

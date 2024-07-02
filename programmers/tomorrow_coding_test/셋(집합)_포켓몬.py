"""포켓몬
https://school.programmers.co.kr/tryouts/85923/challenges?language=python3
"""


def solution(nums: list[int]):
    """
    combinations 으로 일일이 다 확인할 필요는 없다.
    """
    max_num = len(nums) // 2
    unique_nums = set(nums)
    unique_nums_len = len(unique_nums)
    if unique_nums_len <= max_num:
        return unique_nums_len

    return max_num


if __name__ == '__main__':
    assert solution([3,1,2,3]) == 2
    assert solution([3,3,3,2,2,4]) == 3
    assert solution([3,3,3,2,2,2]) == 2

"""과일장수
"""


def solution(nums: list[int]) -> int:
    return min(len(set(nums)), len(nums) // 2)


if __name__ == '__main__':
    assert solution([3,3,3,2,2,2]) == 2
    assert solution([3,3,3,2,2,4]) == 3
    assert solution([3,3,3,2,2,2]) == 2

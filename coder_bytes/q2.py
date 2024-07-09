"""카프리카 루틴 6174
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(num: int) -> int:
    n = num
    count = 0
    while n - 6174:
        n_str = f"{n:04d}"
        n_asc = int(''.join(sorted(n_str)))
        n_des = int(''.join(sorted(n_str, reverse=True)))
        n = max(n_asc, n_des) - min(n_asc, n_des)
        count += 1

    return count


if __name__ == '__main__':
    assert solution(3524) == 3

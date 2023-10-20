"""
"""
from utils import prvalue


@prvalue()
def solution(my_string: str, pat: str):
    len_str, len_pat = len(my_string), len(pat)
    if len_str < len_pat:
        return 0

    return 1 if pat.lower() in my_string.lower() else 0


if __name__ == '__main__':
    assert solution("AbCdEfG", "aBc") == 1
    assert solution("aaAA", "aaaaa") == 0

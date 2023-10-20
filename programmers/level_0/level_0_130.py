"""
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(my_string: str, pat: str):
    index = my_string.rfind(pat)
    return my_string[:index] + pat


if __name__ == '__main__':
    solution("AbCdEFG", "dE")
    solution("AAAAaaaa", "a")
    solution("bAAAAaaaa", "b")
    solution("AAAAbaaaab", "b")

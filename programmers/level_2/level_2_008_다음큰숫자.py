"""다음 큰 숫자
https://school.programmers.co.kr/learn/courses/30/lessons/12911
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(n: int):

    def convert_binary(num: int) -> str:
        return str(bin(num)[2:])

    answer = 0
    count = convert_binary(n).count('1')
    for i in range(n + 1, 1000000 + 1):
        if count == convert_binary(i).count('1'):
            answer = i
            break

    return answer


if __name__ == '__main__':
    assert solution(78) == 83
    assert solution(15) == 23

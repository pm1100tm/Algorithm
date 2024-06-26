"""숫자 짝꿍
https://school.programmers.co.kr/learn/courses/30/lessons/131128
"""
from utils import prvalue
from collections import defaultdict


@prvalue(print_result=True)
def solution(x: str, y: str) -> str:
    start_index_map = defaultdict(int)
    answer = []

    def operation(target: str, compare: str) -> None:
        for char in target:
            start_index = start_index_map[char]
            ret = compare.find(char, start_index)
            if ret != -1:
                start_index_map[char] = ret + 1
                answer.append(char)

    operation(x, y) if len(x) < len(y) else operation(y, x)

    if not answer:
        return '-1'

    check = list(set(answer))
    if len(check) == 1 and check[0] == '0':
        return '0'

    return ''.join(sorted(answer, reverse=True))


def solution2(x: str, y: str) -> str:
    answer = ''
    for i in range(9, -1, -1):
        str_num = str(i)
        answer += str_num * min(x.count(str_num), y.count(str_num))

    if not answer:
        return '-1'
    if answer.count('0') == len(answer):
        return '0'

    return answer


if __name__ == '__main__':
    assert solution('100', '2345') == '-1'
    assert solution('100', '203045') == '0'
    assert solution('100', '123450') == '10'
    assert solution('12321', '42531') == '321'
    assert solution('5525', '1255') == '552'

    assert solution2('100', '2345') == '-1'
    assert solution2('100', '203045') == '0'
    assert solution2('100', '123450') == '10'
    assert solution2('12321', '42531') == '321'
    assert solution2('5525', '1255') == '552'

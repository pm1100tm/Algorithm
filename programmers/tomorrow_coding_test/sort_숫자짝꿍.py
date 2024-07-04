"""숫자 짝꿍
https://school.programmers.co.kr/tryouts/85942/challenges?language=python3
"""
import pytest
from collections import Counter
from utils import prvalue


@prvalue(print_result=True)
def solution(x: str, y: str) -> str:
    """
    시간 초과: case 11 ~ 15
    """
    answer = ''
    x_count, y_count = Counter(x), Counter(y)

    for n in '9876543210':
        if (n in x_count) and (n in y_count):
            common_count = min(x_count[n], y_count[n])
            answer += common_count * n

    if not answer:
        return '-1'

    if int(answer) == 0:
        return '0'

    return answer


@prvalue(print_result=True)
def solution2(x: str, y: str) -> str:
    """
    위의 solution 의 풀이방식에서 시간 초과가 발생하는 주된 이유는 Counter 객체를 사용하여 빈도수를
    계산하고, 이를 반복적으로 접근하는 과정에서 추가적인 시간이 소요되기 때문이다.
    반면, 본 풀이방법에서는 각 문자의 빈도를 직접 계산하고 바로 사용한다. 이는 특히 문자열의 길이가
    매우 길 경우에 두드러진다. 더 단순하고 직접적인 빈도 계산 방식 덕분에, 본 풀이방법이 더 효율적으로
    동작한다.
    """
    answer = ''
    for char in '9876543210':
        count = min(x.count(char), y.count(char))
        answer += char * count

    if not answer:
        return '-1'
    if answer[0] == '0':
        return '0'

    return answer


@pytest.mark.parametrize(
    'x, y, expected',
    [
        ('100', '2345', '-1'),
        ('100', '203045', '0'),
        ('100', '123450', '10'),
        ('12321', '42531', '321'),
        ('5525', '1255', '552'),
    ]
)
def test_solution(x, y, expected):
    assert solution2(x, y) == expected, 'failed'

"""
3x 마을 사람들은 3을 저주의 숫자라고 생각하기 때문에 3의 배수와 숫자 3을 사용하지 않습니다.
3x 마을 사람들의 숫자는 다음과 같습니다.
10  3x  10  3x
1	1	6	8
2	2	7	10
3	4	8	11
4	5	9	14
5	7	10	16

정수 n이 매개변수로 주어질 때, n을 3x 마을에서 사용하는 숫자로 바꿔 return하도록 solution 함수를
완성해주세요.

제한사항
- 1 ≤ n ≤ 100
"""
from utils import prvalue


@prvalue(print_result=False)
def solution(n):
    answer = []
    base = 1
    while len(answer) < n:
        if base % 3 != 0 and '3' not in str(base):
            answer.append(base)
        base += 1

    return answer[-1]


def solution2(n: int) -> int:
    answer = 0
    for _ in range(n):
        answer += 1
        while answer % 3 == 0 or '3' in str(answer):
            answer += 1

    return answer


if __name__ == '__main__':
    assert solution2(15) == 25
    assert solution2(40) == 76

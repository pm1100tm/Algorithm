"""
1부터 6까지 숫자가 적힌 주사위가 세 개 있습니다.
세 주사위를 굴렸을 때 나온 숫자를 각각 a, b, c라고 했을 때 얻는 점수는 다음과 같습니다.

세 숫자가 모두 다르다면 a + b + c 점을 얻습니다.
세 숫자 중 어느 두 숫자는 같고 나머지 다른 숫자는 다르다면 (a + b + c) × (a2 + b2 + c2 )점을 얻습니다.
세 숫자가 모두 같다면 (a + b + c) × (a2 + b2 + c2 ) × (a3 + b3 + c3 )점을 얻습니다.
세 정수 a, b, c가 매개변수로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.

a, b, c는 1이상 6이하의 정수입니다.

2	6	1	9
5	3	3	473
4	4	4	110592
"""
from collections import Counter
from utils import prvalue


@prvalue(print_result=True)
def solution(a: int, b: int, c: int) -> int:

    def cal(num: int, op: str) -> int:
        answer = 0
        for i in range(1, num + 1):
            r = a ** i + b ** i + c ** i
            if op == "+":
                answer += r
                continue

            answer = r if not answer else answer * r

        return answer

    counter = Counter(f"{a}{b}{c}")

    if counter.get(f"{a}") == 1 and counter.get(f"{b}") == 1:
        return cal(1, "+")

    if counter.get(f"{a}") == 2 or counter.get(f"{b}") == 2:
        return cal(2, "*")

    if counter.get(f"{a}") == 3:
        return cal(3, "*")


def solution001(a: int, b: int, c: int) -> int:
    set_len = len({a, b, c})
    anwer = sum([a, b, c])
    if set_len == 3:
        return anwer
    elif set_len == 2:
        return anwer * sum([a**2, b**2, c**2])
    else:
        return anwer * sum([a**2, b**2, c**2]) * sum([a**3, b**3, c**3])


if __name__ == '__main__':
    assert solution(2, 6, 1) == 9
    assert solution(5, 3, 3) == 473
    assert solution(4, 4, 4) == 110592

    assert solution001(2, 6, 1) == 9
    assert solution001(5, 3, 3) == 473
    assert solution001(4, 4, 4) == 110592

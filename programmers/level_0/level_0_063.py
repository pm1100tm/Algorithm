"""
주사위 게임 1

1부터 6까지 숫자가 적힌 주사위가 두 개 있습니다.
두 주사위를 굴렸을 때 나온 숫자를 각각 a, b라고 했을 때 얻는 점수는 다음과 같습니다.

a와 b가 모두 홀수라면 a2 + b2 점을 얻습니다.
a와 b 중 하나만 홀수라면 2 × (a + b) 점을 얻습니다.
a와 b 모두 홀수가 아니라면 |a - b| 점을 얻습니다.
두 정수 a와 b가 매개변수로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.

a와 b는 1 이상 6 이하의 정수입니다.

a   b   result
3	5	34
6	1	14
2	4	2
"""
from utils import prvalue


@prvalue()
def solution(a: int, b: int):
    odd = [1, 3, 5]
    if a in odd and b in odd:
        return a**2 + b**2

    if (a not in odd and b in odd) or (a in odd and b not in odd):
        return (a + b) * 2

    return abs(a - b)


@prvalue()
def solution001():
    pass


@prvalue()
def solution002():
    pass


if __name__ == '__main__':
    assert solution(3, 5) == 34
    assert solution(6, 1) == 14
    assert solution(2, 4) == 2

"""
간단한 식 계산하기

문자열 binomial이 매개변수로 주어집니다.
binomial은 "a op b" 형태의 이항식이고 a와 b는 음이 아닌 정수, op는 '+', '-', '*' 중 하나입니다.
주어진 식을 계산한 정수를 return 하는 solution 함수를 작성해 주세요.

0 ≤ a, b ≤ 40,000
0을 제외하고 a, b는 0으로 시작하지 않습니다.

"43 + 12"	55
"0 - 7777"	-7777
"40000 * 40000"	1600000000
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(binomial: str):
    return eval(binomial)


if __name__ == '__main__':
    solution("43 + 12")
    solution("0 - 7777")
    solution("40000 * 40000")

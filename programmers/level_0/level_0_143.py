"""
영어 알파벳으로 이루어진 문자열 str이 주어집니다.
각 알파벳을 대문자는 소문자로 소문자는 대문자로 변환해서 출력하는 코드를 작성해 보세요.
"""
from utils import prvalue


@prvalue(print_result=False)
def solution1():
    str = input()
    print(''.join([s.lower() if s.isupper() else s.upper() for s in str]))


@prvalue(print_result=False)
def solution2():
    print(input().swapcase())


if __name__ == '__main__':
    solution1()
    solution2()

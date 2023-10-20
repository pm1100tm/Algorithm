"""
x 사이의 개수

문자열 myString이 주어집니다.
myString을 문자 "x"를 기준으로 나눴을 때 나눠진 문자열 각각의 길이를 순서대로 저장한 배열을
return 하는 solution 함수를 완성해 주세요.

1 ≤ myString의 길이 ≤ 100,000
myString은 알파벳 소문자로 이루어진 문자열입니다.


"""
from utils import prvalue


@prvalue(print_result=True)
def solution(my_string: str):
    return list(map(lambda x: len(x), my_string.split("x")))


@prvalue(print_result=True)
def solution001(my_string: str):
    return [len(x) for x in my_string.split("x")]


def solution(myString):
    answer = []
    num = 0
    for i in myString:
        if i == "x":
            answer.append(num)
            num = 0
            continue
        num += 1
    return answer+[num]



if __name__ == '__main__':
    assert solution("oxooxoxxox") == [1, 2, 1, 0, 1, 0]
    assert solution("xabcxdefxghi") == [0, 3, 3, 3]

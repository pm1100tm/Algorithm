"""
문자열이 몇 번 등장하는지 세기

문자열 myString과 pat이 주어집니다.
myString에서 pat이 등장하는 횟수를 return 하는 solution 함수를 완성해 주세요.

1 ≤ myString ≤ 1000
1 ≤ pat ≤ 10

"banana"	"ana"	2
"aaaa"	"aa"	3
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(my_string, pat):
    div = len(pat)
    count = 0
    for i in range(len(my_string) - div + 1):
        if my_string[i:div + i] == pat:
            count += 1

    return count


if __name__ == '__main__':
    solution("banana", "ana")
    solution("aaaa", "aa")

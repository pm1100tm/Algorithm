"""컨트롤 제트
https://school.programmers.co.kr/tryouts/85926/challenges?language=python3
"""


def solution(s: str) -> int:
    char_list = s.split(' ')
    stack = []
    for char in char_list:
        if char == 'Z':
            stack.pop()
        else:
            stack.append(int(char))

    return sum(stack)


if __name__ == '__main__':
    assert solution("1 2 Z 3") == 4
    assert solution("10 20 30 40") == 100
    assert solution("10 Z 20 Z 1") == 1
    assert solution("10 Z 20 Z") == 0
    assert solution("-1 -2 -3 Z") == -3

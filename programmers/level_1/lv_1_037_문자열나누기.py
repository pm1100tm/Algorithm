"""문자열 나누기
https://school.programmers.co.kr/learn/courses/30/lessons/140108
"""


def solution(s: str):
    answer = 0
    i = 0
    while i < len(s):
        char = s[i]
        count_cur, count_oth = 0, 0
        while i < len(s):
            if s[i] == char:
                count_cur += 1
            else:
                count_oth += 1

            i += 1
            if count_cur == count_oth:
                answer += 1
                break

        if count_cur != count_oth:
            answer += 1
            break

    return answer


if __name__ == '__main__':
    solution('ba')
    solution('banana')
    solution('abracadabra')
    solution('aaabbaccccabba')

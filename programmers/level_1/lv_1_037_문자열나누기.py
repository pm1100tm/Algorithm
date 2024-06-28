"""문자열 나누기
https://school.programmers.co.kr/learn/courses/30/lessons/140108
https://school.programmers.co.kr/tryouts/85896/challenges
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


def solution2(s: str) -> int:
    count = 0
    i = 0
    base_index = 0
    temp = ''

    while i < len(s):
        x = s[base_index]
        temp += s[i]

        count_cur = temp.count(x)
        count_oth = len(temp) - count_cur
        if count_cur != count_oth:
            i += 1
        else:
            count += 1
            temp = ''
            i += 1
            base_index = i

    if temp:
        count += 1

    return count


def solution3(s: str) -> int:
    count = 0
    i = 0
    n = len(s)

    while i < n:
        x = s[i]
        count_x = 0
        count_other = 0
        j = i

        while j < n:
            if s[j] == x:
                count_x += 1
            else:
                count_other += 1

            if count_x == count_other:
                break
            j += 1

        i = j + 1 # move i to the next segment
        count += 1

    return count


if __name__ == '__main__':
    assert solution('banana') == 3
    assert solution('abracadabra') == 6
    assert solution('aaabbaccccabba') == 3

    assert solution2('banana') == 3
    assert solution2('abracadabra') == 6
    assert solution2('aaabbaccccabba') == 3

    assert solution3('banana') == 3
    assert solution3('abracadabra') == 6
    assert solution3('aaabbaccccabba') == 3

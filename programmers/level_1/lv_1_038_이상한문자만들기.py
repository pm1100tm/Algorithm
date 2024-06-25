"""이상한 문자 만들기
https://school.programmers.co.kr/learn/courses/30/lessons/12930
"""


def solution(string: str):
    answer = []
    for strs in string.split():
        ret = ''
        for i, char in enumerate(strs):
            char: str
            if i % 2 == 0:
                ret += char.upper()
            else:
                ret += char.lower()

        answer.append(ret)

    return ' '.join(answer)


if __name__ == '__main__':
    assert solution('try hello world') == 'TrY HeLlO WoRlD'

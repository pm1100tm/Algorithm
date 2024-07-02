"""중복된 문자 제거
https://school.programmers.co.kr/tryouts/85921/challenges?language=python3
"""


def solution(my_string: str):
    """
    순서가 필요하기 때문에, set 와 list 를 활용한다.
    """
    unique = set()
    answer = ''
    for char in my_string:
        if char in unique:
            continue

        unique.add(char)
        answer += char

    return answer


if __name__ == '__main__':
    assert solution('people') == 'peol'
    assert solution('We are the world') == 'We arthwold'

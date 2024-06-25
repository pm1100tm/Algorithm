"""신규아이디추천
https://school.programmers.co.kr/learn/courses/30/lessons/72410
"""
import re


def solution(new_id: str) -> str:
    new_id = new_id.lower()
    new_id = re.sub('[~!@#$%^&*()=+\[\]{}:?,<>/]', '', new_id)

    if not new_id:
        return 'a'

    new_id = re.sub('[\.]{2,}', '.', new_id)

    if len(new_id) > 1 and new_id[0] == '.':
        new_id = re.sub('^[\.]', '', new_id)

    if len(new_id) > 1 and new_id[-1] == '.':
        new_id = re.sub('[\.]$', '', new_id)

    if len(new_id) == 1 and new_id == '.':
        new_id = 'a'

    if len(new_id) > 15:

        new_id = new_id[:15]

        if new_id[-1] == '.':
            new_id = re.sub('[\.]$', '', new_id)

        return new_id

    if len(new_id) < 3:

        while len(new_id) < 3:
            new_id += new_id[-1]

    return new_id


def solution2(new_id: str) -> str:
    target_id = new_id
    target_id = target_id.lower()

    # 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
    target_id = re.sub('[^a-z0-9 \-_.]', '', target_id)

    # 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    target_id = re.sub('\.+', '.', target_id)

    # 마침표(.)가 처음이나 끝에 위치한다면 제거
    target_id = re.sub('^\.*|\.*$', '', target_id)

    # new_id가 빈 문자열이라면, new_id에 "a"를 대입
    # 길이가 16자 이상이면, new_id의 첫 15개의 문자 제외 나머지 문자들 모두 제거
    target_id = 'a' if not len(target_id) else target_id[:15]

    # 제거 후 마침표(.)가 끝에 위치한다면 끝에 위치한 마침표(.) 문자 제거
    target_id = re.sub('^\.*|\.*$', '', target_id)

    # new_id의 길이가 2자 이하라면, 마지막 문자를 길이가 3이 될 때까지 반복해서 붙임
    while len(target_id) < 3:
        last_char = target_id[-1]
        target_id += last_char
    print(target_id)
    return target_id


if __name__ == '__main__':
    assert solution2("...!@BaT#*..y.abcdefghijklm") == "bat.y.abcdefghi"
    assert solution2("z-+.^.") == "z--"
    assert solution2("=.=") == "aaa"
    assert solution2("123_.def") == "123_.def"
    assert solution2("abcdefghijklmn.p") == "abcdefghijklmn"

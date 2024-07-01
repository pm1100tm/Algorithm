"""로그인 성공?
https://school.programmers.co.kr/tryouts/85912/challenges
"""


def solution(id_pw, db):
    user_id, pw = id_pw
    db_map = {user_id: pw for user_id, pw in db}

    db_user_pw = db_map.get(user_id)

    if not db_user_pw:
        return 'fail'
    if db_user_pw != pw:
        return 'wrong pw'

    return 'login'


if __name__ == '__main__':
    solution(
        ["meosseugi", "1234"],
        [["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]],
    )

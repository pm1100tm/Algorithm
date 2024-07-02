"""전화번호 목록
https://school.programmers.co.kr/tryouts/85917/challenges?language=python3
"""
from utils import prvalue


def solution(phone_book: list[str]):
    answer = True
    sorted_phone_book = sorted(phone_book, key=lambda x: len(x))
    for i in range(len(sorted_phone_book)):
        for j in range(i+1, len(sorted_phone_book)):
            if sorted_phone_book[j].startswith(sorted_phone_book[i]):
                answer = False
                break

        if not answer:
            break

    return answer


@prvalue(print_result=True)
def solution2(phone_book: list[str]):
    phone_dict = {phone: 0 for phone in phone_book}
    for phone in phone_book:
        prefix = ''
        for digit in phone:
            prefix += digit
            if prefix in phone_dict and prefix != phone:
                return False

    return True


if __name__ == '__main__':
    solution(["119", "97674223", "1195524421"])
    solution(["123","456","789"])
    solution(["12","123","1235","567","88"])

    solution2(["119", "97674223", "1195524421"])
    solution2(["123","456","789"])
    solution2(["12","123","1235","567","88"])

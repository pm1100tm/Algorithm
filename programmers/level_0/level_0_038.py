"""
숨어있는 숫자의 덧셈 (1)

문자열 my_string이 매개변수로 주어집니다.
my_string안의 모든 자연수들의 합을 return하도록 solution 함수를 완성해주세요.

1 ≤ my_string의 길이 ≤ 1,000
my_string은 소문자, 대문자 그리고 한자리 자연수로만 구성되어있습니다.
"""
from utils import prvalue


@prvalue(print_time=True)
def solution(my_string: str) -> int:
    return sum([int(s) for s in my_string if s.isdigit()])


@prvalue(print_time=True)
def solution001(my_string: str) -> int:
    number = ['0','1','2','3','4','5','6','7','8','9']
    ret_list = [int(i) for i in range(len(my_string)) if my_string[i] in number]
    return sum(ret_list)


if __name__ == '__main__':
    assert solution("aAb1B2cC34oOp") == 10
    assert solution("1a2b3c4d123") == 16

    import random
    import string

    def generate_random_string(length):
        characters = string.ascii_letters + string.digits
        random_sstr = ''.join(random.choice(characters) for _ in range(length))
        return random_sstr

    random_string = generate_random_string(3000000)

    assert solution(random_string) # win
    assert solution001(random_string)

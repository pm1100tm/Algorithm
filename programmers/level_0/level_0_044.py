"""
이어 붙인 수

정수가 담긴 리스트 num_list가 주어집니다.
num_list의 홀수만 순서대로 이어 붙인 수와 짝수만 순서대로 이어 붙인 수의 합을 return하도록
solution 함수를 완성해주세요.

2 ≤ num_list의 길이 ≤ 10
1 ≤ num_list의 원소 ≤ 9
num_list에는 적어도 한 개씩의 짝수와 홀수가 있습니다.

홀수만 이어 붙인 수는 351이고 짝수만 이어 붙인 수는 42입니다. 두 수의 합은 393입니다.
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(num_list: list[int]) -> int:
    odd_ = "".join(
        [str(x) for x in list(filter(lambda x: x % 2 != 0, num_list))]
    )
    even = "".join(
        [str(x) for x in list(filter(lambda x: x % 2 == 0, num_list))]
    )
    return sum([int(odd_),  int(even)])


@prvalue()
def solution001(num_list: list[int]) -> int:
    str_odd_: str = ""
    str_even: str = ""
    for n in num_list:
        if n % 2 == 0:
            str_odd_ += str(n)
        else:
            str_even += str(n)

    return int(str_odd_) + int(str_even)


@prvalue()
def solution002():
    pass


if __name__ == '__main__':
    assert solution([3, 4, 5, 2, 1]) == 393
    assert solution([5, 7, 8, 3]) == 581

    assert solution001([3, 4, 5, 2, 1]) == 393
    assert solution001([5, 7, 8, 3]) == 581

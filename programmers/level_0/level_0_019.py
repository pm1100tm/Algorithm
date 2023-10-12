"""
짝수 홀수 개수

정수가 담긴 리스트 num_list가 주어질 때, num_list의 원소 중 짝수와 홀수의 개수를 담은 배열을
return 하도록 solution 함수를 완성해보세요.
"""
from utils import prvalue


@prvalue()
def solution001(num_list: list[int]) -> list[int]:
    num_even: int = len(list(filter(lambda x: x % 2 == 0, num_list)))
    return [num_even, len(num_list) - num_even]


@prvalue()
def solution002(num_list: list[int]) -> list[int]:
    ret = [0, 0]

    def acc(obj, index):
        obj[index] += 1

    [acc(ret, num % 2) for num in num_list]

    return ret


@prvalue()
def solution003(num_list: list[int]) -> list[int]:
    ret = [0, 0]
    acc = lambda obj, index: obj.__setitem__(index, obj[index] + 1)
    [acc(ret, num % 2) for num in num_list]

    return ret


@prvalue()
def solution004(num_list: list[int]) -> list[int]:
    div_num_list = list(map(lambda v: v % 2, num_list))
    return [div_num_list.count(0), div_num_list.count(1)]


if __name__ == '__main__':
    assert [2, 3] == solution001([1, 2, 3, 4, 5])
    assert [0, 4] == solution001([1, 3, 5, 7])
    assert [2, 3] == solution002([1, 2, 3, 4, 5])
    assert [0, 4] == solution002([1, 3, 5, 7])
    assert [2, 3] == solution003([1, 2, 3, 4, 5])
    assert [0, 4] == solution003([1, 3, 5, 7])
    assert [2, 3] == solution003([1, 2, 3, 4, 5])
    assert [0, 4] == solution003([1, 3, 5, 7])
    assert [2, 3] == solution004([1, 2, 3, 4, 5])
    assert [0, 4] == solution004([1, 3, 5, 7])

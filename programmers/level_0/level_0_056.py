"""
배열의 원소만큼 추가하기

아무 원소도 들어있지 않은 빈 배열 X가 있습니다. 양의 정수 배열 arr가 매개변수로 주어질 때,
arr의 앞에서부터 차례대로 원소를 보면서 원소가 a라면 X의 맨 뒤에 a를 a번 추가하는 일을 반복한 뒤의
배열 X를 return 하는 solution 함수를 작성해 주세요.

1 ≤ arr의 길이 ≤ 100
1 ≤ arr의 원소 ≤ 100
"""
from utils import prvalue


@prvalue(print_time=True)
def solution(arr: list[int]) -> list[int]:
    result: list[int] = []
    for a in arr:
        result += [a for _ in range(a)]

    return result


@prvalue(print_time=True)
def solution001(arr: list[int]) -> list[int]:
    answer = []

    def add_list(v: int):
        nonlocal answer
        answer += [v] * v

    [add_list(a) for a in arr]

    return answer


@prvalue(print_time=True)
def solution002(arr: list[int]) -> list[int]:
    answer = []
    for a in arr:
        answer += [a] * a

    return answer


if __name__ == '__main__':
    assert solution([5, 1, 4]) == [5, 5, 5, 5, 5, 1, 4, 4, 4, 4]
    assert solution([6, 6]) == [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
    assert solution([1]) == [1]

    assert solution001([5, 1, 4]) == [5, 5, 5, 5, 5, 1, 4, 4, 4, 4]
    assert solution001([6, 6]) == [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
    assert solution001([1]) == [1]

    assert solution002([5, 1, 4]) == [5, 5, 5, 5, 5, 1, 4, 4, 4, 4]
    assert solution002([6, 6]) == [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
    assert solution002([1]) == [1]

    # check time
    print(f"{'*' * 50}")
    import random
    random.seed()

    int_list = [random.randrange(1, 100) for _ in range(1600000)]
    solution(int_list)
    solution001(int_list)
    solution002(int_list)
    # It's fastest to make a loop only go once if it can go just once,
    # even though it my eat more memory.

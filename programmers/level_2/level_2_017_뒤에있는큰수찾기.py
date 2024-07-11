"""뒤에 있는 큰 수 찾기
https://school.programmers.co.kr/learn/courses/30/lessons/154539
- idea
Initialize result list with -1
Stack
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(numbers: list[int]):
    """
    시간 초과
    """
    answer = []
    for i, n in enumerate(numbers):
        biggest_num = None
        for num in numbers[i:]:
            if num > n:
                biggest_num = num
                break

        answer.append(biggest_num if biggest_num is not None else -1)

    return answer


@prvalue(print_result=True)
def solution2(numbers: list[int]):
    """
    시간 초과: case 20~23
    """
    answer = []
    for i, n in enumerate(numbers[:len(numbers) - 1]):
        acc = i + 1
        nearest_bigger_num = -1
        while acc < len(numbers):
            if n < numbers[acc]:
                nearest_bigger_num = numbers[acc]
                break
            acc += 1

        answer.append(nearest_bigger_num)

    return answer + [-1]


@prvalue(print_result=True)
def solution3(numbers: list[int]):
    """
    역순으로 순회하는 방법
    """
    # 결과 배열을 초기화. 모든 요소에 대해 가까운 큰 숫자를 저장하며, 큰 숫자가 존재하지 않는다면 -1값을
    # 설정하기 때문에, 배열의 길이 만큼 -1값을 넣어준다.
    n = len(numbers)
    answer = [-1] * n

    # 스택은 배열에 있는 요소의 인덱스를 저장한다.
    stack = []

    # 배열의 오른쪽에서 왼쪽으로 이동한다. 각 요소에 대해서 스택이 비어있지 않고, 스택의 맨 위 요소에
    # 해당하는(index) 값이, 현재 값보다 작다면 스택에서 꺼낸다. (pop)
    # 그 후, 스택이 비어 있지 않으면 스택의 맨 위가 가장 가까운 큰 수이다.
    for i in range(n-1, -1, -1):
        # 스택이 비어있지 않을 때
        # 현재 요소가 스택 최상단 인덱스에 해당하는 값보다 크다면, 차후 진행되는 요소의 가장 가까운
        # 큰 값이 현재 요소가 된다.
        # 현재 요소가 스택 최상단 인덱스에 해당하는 값보다 작다면, 스택은 계속 쌓인다.
        while stack and numbers[i] >= numbers[stack[-1]]:
            stack.pop()

        if stack:
            answer[i] = numbers[stack[-1]]

        stack.append(i)

    return answer


@prvalue(print_result=True)
def solution4(numbers: list[int]):
    """
    정순으로 순회하는 방법
    """
    stack = []
    answer = [-1] * len(numbers)
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]

        # 현재 값이 이전 값보다 크지 않은 경우, 현재의 인덱스를 저장하여,
        # 현재 값이 이전 값보다 큰 경우 후 처리 할 수 있도록한다.
        stack.append(i)

    return answer


if __name__ == '__main__':
    assert solution3([2, 3, 3, 5]) == [3, 5, 5, -1]
    assert solution3([9, 1, 5, 3, 6, 2]) == [-1, 5, 6, 6, -1, -1]
    assert solution3([9, 1, 5, 5, 3, 6, 10]) == [10, 5, 6, 6, 6, 10, -1]
    assert solution3([10, 9, 8, 7, 6, 5, 5]) == [-1, -1, -1, -1, -1, -1, -1]

    assert solution4([2, 3, 3, 5]) == [3, 5, 5, -1]
    assert solution4([9, 1, 5, 3, 6, 2]) == [-1, 5, 6, 6, -1, -1]
    assert solution4([9, 1, 5, 5, 3, 6, 10]) == [10, 5, 6, 6, 6, 10, -1]
    assert solution4([10, 9, 8, 7, 6, 5, 5]) == [-1, -1, -1, -1, -1, -1, -1]

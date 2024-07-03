"""햄버거 만들기
https://school.programmers.co.kr/tryouts/85928/challenges?language=python3
"""


def solution(ingredient: list[int]) -> int:
    """부분 성공: case 3 ~ 12 실패
    """
    answer = 0
    ingre = ingredient[::-1]
    hamburgar = [1, 2, 3, 1]
    start, stack = 0, []
    while ingre:
        if len(stack) < 4:
            stack.append(ingre.pop())
            continue
        if stack[start: start + 4] != hamburgar:
            stack.append(ingre.pop())
            start += 1
        else:
            stack = stack[:start]
            start = 0
            answer += 1

    if stack[len(stack) - 4: len(stack)] == hamburgar:
        answer += 1

    return answer


def solution2(ingredient: list[int]) -> int:
    """시간 초과: case 4, 5, 7, 12
    """
    ingre = ''.join([str(x) for x in ingredient])
    answer = 0
    while True:
        old_len = len(ingre)
        ingre = ingre.replace('1231', '', 1)
        new_len = len(ingre)
        if old_len > new_len:
            answer += 1
            continue
        break

    return answer


def solution3(ingredient: list[int]) -> int:
    """시간 초과: case 5, 12
    """
    stack = []
    count = 0
    hamburgar = [1, 2, 3, 1]
    for v in ingredient:
        stack.append(v)
        if len(stack) >= 4 and stack[-4:] == hamburgar:
            stack = stack[:-4]
            count += 1

    return count


from collections import deque


def solution4(ingredient: list[int]) -> int:
    """성공
    """
    ingre = deque(ingredient)
    stack = []
    count = 0

    while ingre:
        stack.append(ingre.popleft())
        if len(stack) >= 4 and stack[-4:] == [1, 2, 3, 1]:
            for _ in range(4):
                stack.pop()
            count += 1

    return count


def solution5(ingredient: list[int]) -> int:
    """성공
    solution3 과의 시간 복잡도의 주요 차이점은 아래와 같다.
    - 햄버거 패턴이 감지되어 stack 을 제거하는 방식에서 차이가 발생한다.
    - pop() 메서드는 O(1) 의 시간 복잡도이며, 이것을 4번 반복한다.
    - 슬라이싱은 새로운 배열을 생성하고 시간 복잡도가 O(n)이며, n 은 stack 의 길이이다.
    - 따라서, 햄버거 패턴이 감지되어 stack을 제거할 때 마다 새로운 배열을 생성하는데, 이는 더 많은
      메모리 할당/해제를 의미하며 오버헤드가 발생한다.
    - 또한, 슬라이딩 연산은 루프 내에서 O(n)의 복잡성을 추가하므로, 햄버거 패턴이 자주 발견되는 경우
      전체 시간 복잡도가 O(n^2)에 가까워진다.
    - 따라서, stack배열을 조정할 때, 새로운 배열을 만드는 것이 아니라, pop 연산으로 요소를 제거하여
      조정하는 것이 훨씬 빠르다.
    """
    stack = []
    count = 0
    hamburgar = [1, 2, 3, 1]

    for v in ingredient:
        stack.append(v)
        if stack[-4:] == hamburgar:
            count += 1
            for _ in range(4):
                stack.pop()

    return count


if __name__ == '__main__':
    # assert solution([1, 2, 1, 2, 3, 3, 3, 1]) == 0
    # assert solution([1, 3, 2, 3, 1]) == 0
    # assert solution([1, 2, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 3, 3, 1]) == 2
    # assert solution([1, 1, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1]) == 3
    # assert solution([1, 2, 1, 2, 3, 1, 3, 1]) == 2
    # assert solution([1, 2, 1, 2, 3, 1, 3, 1, 2, 3, 1, 1]) == 2
    # assert solution([1, 2, 3, 2, 1]) == 0
    # assert solution([2, 1, 2, 1, 1, 2, 3, 1, 2, 3, 1]) == 2
    # assert solution(
    #     [1, 1, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1]
    # ) == 5

    # assert solution2([1, 2, 1, 2, 3, 3, 3, 1]) == 0
    # assert solution2([1, 3, 2, 3, 1]) == 0
    # assert solution2([1, 2, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 3, 3, 1]) == 2
    # assert solution2([1, 1, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1]) == 3
    # assert solution2([1, 2, 1, 2, 3, 1, 3, 1]) == 2
    # assert solution2([1, 2, 1, 2, 3, 1, 3, 1, 2, 3, 1, 1]) == 2
    # assert solution2([1, 2, 3, 2, 1]) == 0
    # assert solution2([2, 1, 2, 1, 1, 2, 3, 1, 2, 3, 1]) == 2
    # assert solution2(
    #     [1, 1, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1]
    # ) == 5

    # assert solution3([1, 2, 1, 2, 3, 3, 3, 1]) == 0
    # assert solution3([1, 3, 2, 3, 1]) == 0
    # assert solution3([1, 2, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 3, 3, 1]) == 2
    # assert solution3([1, 1, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1]) == 3
    # assert solution3([1, 2, 1, 2, 3, 1, 3, 1]) == 2
    # assert solution3([1, 2, 1, 2, 3, 1, 3, 1, 2, 3, 1, 1]) == 2
    # assert solution3([1, 2, 3, 2, 1]) == 0
    # assert solution3([2, 1, 2, 1, 1, 2, 3, 1, 2, 3, 1]) == 2
    # assert solution3(
    #     [1, 1, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1]
    # ) == 5

    assert solution4([1, 2, 1, 2, 3, 3, 3, 1]) == 0
    assert solution4([1, 3, 2, 3, 1]) == 0
    assert solution4([1, 2, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 3, 3, 1]) == 2
    assert solution4([1, 1, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1]) == 3
    assert solution4([1, 2, 1, 2, 3, 1, 3, 1]) == 2
    assert solution4([1, 2, 1, 2, 3, 1, 3, 1, 2, 3, 1, 1]) == 2
    assert solution4([1, 2, 3, 2, 1]) == 0
    assert solution4([2, 1, 2, 1, 1, 2, 3, 1, 2, 3, 1]) == 2
    assert solution4(
        [1, 1, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1]
    ) == 5

    assert solution5([1, 2, 1, 2, 3, 3, 3, 1]) == 0
    assert solution5([1, 3, 2, 3, 1]) == 0
    assert solution5([1, 2, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 3, 3, 1]) == 2
    assert solution5([1, 1, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1]) == 3
    assert solution5([1, 2, 1, 2, 3, 1, 3, 1]) == 2
    assert solution5([1, 2, 1, 2, 3, 1, 3, 1, 2, 3, 1, 1]) == 2
    assert solution5([1, 2, 3, 2, 1]) == 0
    assert solution5([2, 1, 2, 1, 1, 2, 3, 1, 2, 3, 1]) == 2
    assert solution5(
        [1, 1, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1]
    ) == 5

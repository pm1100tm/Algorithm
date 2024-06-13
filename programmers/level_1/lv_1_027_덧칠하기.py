"""덧칠하기
페인트가 칠해진 길이가 n미터인 벽이 있습니다. 페인트가 벗겨진 벽에 페인트를 덧칠하기로 했습니다.
벽에 페인트를 칠하는 롤러의 길이는 m미터이고, 롤러로 벽에 페인트를 한 번 칠하는 규칙은 다음과 같습니다.
- 롤러가 벽에서 벗어나면 안 됩니다.
- 구역의 일부분만 포함되도록 칠하면 안 됩니다.
정수 n, m과 다시 페인트를 칠하기로 정한 구역들의 번호가 담긴 정수 배열 section이 매개변수로 주어질 때
롤러로 페인트칠해야 하는 최소 횟수를 return 하는 solution 함수를 작성해 주세요.

제한사항
- 1 ≤ m ≤ n ≤ 100,000
- 1 ≤ section의 길이 ≤ n
  - 1 ≤ section의 원소 ≤ n
  - section의 원소는 페인트를 다시 칠해야 하는 구역의 번호입니다.
  - section에서 같은 원소가 두 번 이상 나타나지 않습니다.
  - section의 원소는 오름차순으로 정렬되어 있습니다.

algorithm - greedy
approach
- Use a greedy strategy to place the roller in such a way that it covers
  as many sections as possible in each pass.
- Start from the first section that needs to be painted and place the roller to cover
  as many subsequent sections as possible, then move to the next uncovered section
  and repeat.
"""
from collections import deque


def solution(n: int, m: int, section: list[int]) -> int:
    roller_count = 0
    index = 0

    while index < len(section):
        roller_count += 1
        start = section[index]

        while index < len(section) and section[index] < start + m:
            index += 1

    return roller_count


def solution2(n: int, m: int, section: list[int]) -> int:
    answer = 0
    q_section = deque(section)

    while q_section:
        start = q_section.popleft()
        while q_section:
            if q_section[0] >= start + m:
                break

            q_section.popleft()

        answer += 1

    return answer


if __name__ == '__main__':
    assert solution(8, 4, [2, 3, 6]) == 2
    assert solution(5, 4, [1, 3]) == 1
    assert solution(4, 1, [1, 2, 3, 4]) == 4
    assert solution2(8, 4, [2, 3, 6]) == 2
    assert solution2(5, 4, [1, 3]) == 1
    assert solution2(4, 1, [1, 2, 3, 4]) == 4

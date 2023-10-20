"""
특별한 이차원 배열 1

정수 n이 매개변수로 주어질 때, 다음과 같은 n × n 크기의 이차원 배열 arr를
return 하는 solution 함수를 작성해 주세요.
arr[i][j] (0 ≤ i, j < n)의 값은 i = j라면 1, 아니라면 0입니다.

1 ≤ n ≤ 100

3	[[1, 0, 0], [0, 1, 0], [0, 0, 1]]
6	[[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1]]
1	[[1]]
"""
from utils import prvalue


@prvalue(print_time=True)
def solution(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


@prvalue(print_time=True)
def solution001(n):
    answer = []
    for i in range(n):
        answer.append([0 for _ in range(n)])

    for i in range(n):
        answer[i][i] = 1

    return answer


if __name__ == '__main__':
    # assert solution(3) == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    # assert solution(6) == [[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1]]
    # assert solution(1) == [[1]]
    # assert solution001(3) == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    # assert solution001(6) == [[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1]]
    # assert solution001(1) == [[1]]

    solution(10000) # 2.0861947536
    solution001(10000) # 1.5008270741

    """
    solution 과 solution001 의 속도를 비교해보면, solution001 이 훨씬 빠르다는 것을 확인할 수 있다.
    solution:
     리스트 컴프리헨션을 사용하면 한 번에 모든 값을 생성하므로 코드가 간결하게 읽기 쉽다. =
     그러나 큰 n 값에 대하여, 큰 크기의 리스트를 한 번에 생성하므로, 메모리 사용량이 더 많을 수 있다.
    
    solution001
     0 으로 초기화된 2차원 리스트를 생성하고, 그 후에 대각선으로 1을 할당한다.
     한 번에 모든 값을 생성하지 않고 초기화 후 값을 할당하므로 메모리 사용량이 더 효율적이다.
     따라서 작은 n 값에 대해서는 성능 차이가 미미할 수 있지만, 큰 값에 대해서는 메모리 사용량과
     실행속도 면에서 더 효율적일 수 있다.
    """

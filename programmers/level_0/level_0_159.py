"""
정수 n을 기준으로 n과 가까운 수부터 정렬하려고 합니다. 이때 n으로부터의 거리가 같다면 더 큰 수를 앞에
오도록 배치합니다. 정수가 담긴 배열 numlist와 정수 n이 주어질 때 numlist의 원소를 n으로부터 가까운
순서대로 정렬한 배열을 return하도록 solution 함수를 완성해주세요.

제한사항
- 1 ≤ n ≤ 10,000
- 1 ≤ numlist의 원소 ≤ 10,000
- 1 ≤ numlist의 길이 ≤ 100
- numlist는 중복된 원소를 갖지 않습니다.
"""
from utils import prvalue


@prvalue(print_result=False)
def solution(numlist: list[int], n: int):
    """
    두번 째 정렬 키 값 -x 는, 기본적으로 오름차순으로 정렬되기 때문에 값을 반전 시키기 위함.
    큰 값을 반전시켜서 작은 값으로 만들어 앞에 위치하도록 하기 위한 트릭.
    """
    return sorted(numlist, key=lambda x: (abs(x - n), -x))


if __name__ == '__main__':
    assert solution([1, 2, 3, 4, 5, 6], 4) == [4, 5, 3, 6, 2, 1]
    assert (
        solution([10000, 20, 36, 47, 40, 6, 10, 7000], 30)
        == [36, 40, 20, 47, 10, 6, 7000, 10000]
    )

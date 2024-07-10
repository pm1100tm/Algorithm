"""카프리카 상수 495, 6174
0부터 9까지의 정수 중 세 개의 수를 고르되, 같은 수를 세 번 고르지 말아야 한다. 그 세 수를 큰 순서대로
배열하여 세 자리 자연수를 만들고, 작은 순서대로 배열하여 또 다른 세 자리 자연수를 만든다.
그런 다음 이 두 수의 차를 구한다. 두 수의 차가 되는 세 자리 자연수 역시 큰 순서대로 다시 배열하여 새로운
세 자리 자연수를 만든다. 이 자연수의 배열을 역순으로 하여 또 다른 세 자리 자연수를 만들고 이 두 수의 차를
구한다. 단, 두 수의 차가 세 자리가 되지 않는다면, 세 자리가 되기 위해 부족한 자리를 모두 0으로 간주한다.
이 과정을 계속 반복하면 결국 495가 된다.
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(num: int) -> int:
    n = num
    count = 0
    while n - 6174:
        n_str = f"{n:04d}"
        n_asc = int(''.join(sorted(n_str)))
        n_des = int(''.join(sorted(n_str, reverse=True)))
        n = max(n_asc, n_des) - min(n_asc, n_des)
        count += 1

    return count


if __name__ == '__main__':
    assert solution(3524) == 3

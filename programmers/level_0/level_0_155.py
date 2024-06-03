"""
프로그래머스 치킨은 치킨을 시켜먹으면 한 마리당 쿠폰을 한 장 발급합니다. 쿠폰을 열 장 모으면
치킨을 한 마리 서비스로 받을 수 있고, 서비스 치킨에도 쿠폰이 발급됩니다.
시켜먹은 치킨의 수 chicken이 매개변수로 주어질 때 받을 수 있는 최대 서비스 치킨의 수를 return하도록
solution 함수를 완성해주세요.

chicken은 정수입니다.
0 ≤ chicken ≤ 1,000,000

"""
from utils import prvalue


@prvalue(print_result=False)
def solution(chicken):
    service_count = 0
    while True:
        chicken = chicken - 10
        if chicken < 0:
            break
        chicken += 1
        service_count += 1

    return service_count


def solution2(chicken: int) -> int:
    service_chicken_count = 0
    while chicken >= 10:
        quo, rem = divmod(chicken, 10)
        service_chicken_count += quo
        chicken = quo + rem

    return service_chicken_count


def solution3(chicken: int) -> int:
    service, rem = divmod(chicken, 10)

    chicken = service + rem
    if chicken < 10:
        return service

    return solution3(chicken)


if __name__ == '__main__':
    # assert solution(0) == 0
    # assert solution(1) == 0
    # assert solution(9) == 0
    # assert solution(10) == 1
    # assert solution(100) == 11
    # assert solution(1081) == 120

    # assert solution2(0) == 0
    # assert solution2(1) == 0
    # assert solution2(9) == 0
    # assert solution2(10) == 1
    # assert solution2(100) == 11
    # assert solution2(1081) == 120

    assert solution3(0) == 0
    assert solution3(1) == 0
    assert solution3(9) == 0
    assert solution3(10) == 1
    assert solution3(100) == 11
    # assert solution3(1081) == 120

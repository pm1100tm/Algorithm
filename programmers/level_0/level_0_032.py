"""
옷가게 할인 받기

머쓱이네 옷가게는 10만 원 이상 사면 5%, 30만 원 이상 사면 10%, 50만 원 이상 사면 20%를 할인해줍니다.
구매한 옷의 가격 price가 주어질 때, 지불해야 할 금액을 return 하도록 solution 함수를 완성해보세요.

10 ≤ price ≤ 1,000,000
price는 10원 단위로(1의 자리가 0) 주어집니다.
소수점 이하를 버린 정수를 return합니다.
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(price):
    discount_map = {
        100000: 0.05,
        300000: 0.10,
        500000: 0.20,
    }

    k = list(filter(lambda x: price >= x, discount_map.keys()))
    if not k:
        return price

    return int(price * (1 - discount_map[k[-1]]))


@prvalue(print_result=True)
def solution001(price: int) -> int:
    discount_map = {
        500000: 0.2,
        300000: 0.1,
        100000: 0.05,
        0: 0,
    }

    discount_rate = 0
    for k, v in discount_map.items():
        if price >= k:
            discount_rate = v
            break

    answer = int(price * (1 - discount_rate))

    return answer


if __name__ == '__main__':
    assert solution(10) == 10
    assert solution(11) == 11
    assert solution(99999) == 99999
    assert solution(100000) == 95000
    assert solution(150000) == 142500
    assert solution(580000) == 464000

    assert solution001(10) == 10
    assert solution001(11) == 11
    assert solution001(99999) == 99999
    assert solution001(100000) == 95000
    assert solution001(150000) == 142500
    assert solution001(580000) == 464000

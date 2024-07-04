"""양꼬치
머쓱이네 양꼬치 가게는 10인분을 먹으면 음료수 하나를 서비스로 줍니다.
양꼬치는 1인분에 12,000원, 음료수는 2,000원입니다.
정수 n과 k가 매개변수로 주어졌을 때, 양꼬치 n인분과 음료수 k개를 먹었다면 총얼마를 지불해야 하는지
return 하도록 solution 함수를 완성해보세요.
"""
from typing import Final
from utils import prvalue


@prvalue()
def solution001(n: int, k: int) -> int:
    PRICE_MENU_N: Final[int] = 12000
    PRICE_MENU_K: Final[int] = 2000

    drint_count_service: int = (n // 10)
    price_n = n * PRICE_MENU_N
    price_k = k * PRICE_MENU_K
    price_discounted = (drint_count_service * PRICE_MENU_K) * -1

    return price_n + price_k + price_discounted


@prvalue()
def solution002(n: int, k: int) -> int:
    return 12000 * n + 2000 * (k - n // 10)


if __name__ == '__main__':
    solution001(10, 3)
    solution001(64, 6)
    solution002(10, 3)
    solution002(64, 6)

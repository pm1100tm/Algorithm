"""

"""
from utils import prvalue

import math


@prvalue(print_result=False)
def solution(numer1, denom1, numer2, denom2):
    bunmo = denom1 * denom2
    bunja1 = numer1 * (bunmo // denom1)
    bunja2 = numer2 * (bunmo // denom2)
    bunza = bunja1 + bunja2
    gcd = math.gcd(bunmo, bunza)
    answer = [bunza // gcd,bunmo // gcd]
    return answer


def solution2(numer1, denom1, numer2, denom2):
    """
    TODO: Bloging for how to use Fraction
    """
    from fractions import Fraction
    answer = Fraction(numer1, denom1) + Fraction(numer2, denom2)

    return [answer.numerator, answer.denominator]


if __name__ == '__main__':
    case1 = [1, 2, 3, 4]
    case2 = [9, 2, 1, 3]

    assert solution(*case1) == [5, 4]
    assert solution(*case2) == [29, 6]

    assert solution2(*case1) == [5, 4]
    assert solution2(*case2) == [29, 6]

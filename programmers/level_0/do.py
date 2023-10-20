import math


if __name__ == '__main__':
    from functools import reduce

    t1 = [3, 4, 5, 2, 5, 4, 6, 7, 3, 7, 2, 2, 1]
    t2  =[2, 3, 4, 5]

    def dodo(num_list: list[int]):
        if len(num_list) <= 10:
            return reduce(lambda x, y: x * y, num_list)
        else:
            return sum(num_list)

    assert dodo(t1) == 51
    assert dodo(t2) == 120

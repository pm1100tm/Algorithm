x = 3
a  = [3]
b = [3]


def calc1(x):
    x += 4
    return x


def calc2(a):
    print(id(a))
    a[0] += 4
    return a


def calc3(b):
    b = [4]
    return b


if __name__ == '__main__':
    print(x) # 3
    print(calc1(x)) # 7
    print(x) # 3

    print()

    print(a) # [3]
    print(id(a))
    print(calc2(a)) # [7]
    print(a) # [7]

    print()

    print(b) # [3]
    print(calc3(b)) # [4]
    print(b) # [3]
    assert id(calc3(b)) != id(b)

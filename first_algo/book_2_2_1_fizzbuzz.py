def solution1():
    x = 3
    y = 5
    z = x * y
    fizz, buzz = "Fizz", "Buzz"

    for i in range(1, 101):
        if i % z == 0:
            print(f"{fizz}{buzz}")
        elif i % x == 0:
            print(f"{fizz}")
        elif i % y == 0:
            print(f"{buzz}")
        else:
            print(f"{i}")


def solution2():
    x, y, z = 3, 5, 3 * 5
    fizz, buzz = "Fizz", "Buzz"

    for i in range(1, 101):
        if i % z == 0:
            print(f"{fizz}{buzz}", end=" ")
        elif i % x == 0:
            print(f"{fizz}", end=" ")
        elif i % y == 0:
            print(f"{buzz}", end=" ")
        else:
            print(f"{i}", end=" ")


if __name__ == '__main__':
    solution2()

def solution1():
    numbers = set()
    for _ in range(10):
        _, b = divmod(int(input()), 42)
        numbers.add(b)

    print(len(numbers))


def solution2():
    check = [0] * 42
    for i in range(10):
        n = int(input())
        check[n % 42] = 1

    print(sum(check))


if __name__ == '__main__':
    pass

def fibonacci(n: int):
    assert isinstance(n, int), f"Type error {n} is not int"
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    for i in range(1, 8):
        print(fibonacci(i))

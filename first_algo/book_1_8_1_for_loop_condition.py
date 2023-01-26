def for_loop_condition(data: list) -> None:
    assert isinstance(data, list), f"type error, {data} it not list"
    [print(n) if n == 2 else print() for n in data]


if __name__ == '__main__':
    _data = [i for i in range(1, 10) if i % 2 == 0]
    print(_data)
    for_loop_condition(_data)

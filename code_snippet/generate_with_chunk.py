def generate_numbers(start, end):
    for number in range(start, end + 1):
        yield number


def process_chunk(chunk: list[int]) -> list[int]:
    return [x + 3 for x in chunk]


def process():
    start, end = 1, 1000
    numbers_generator = generate_numbers(start, end)
    chunk_size = 10
    processed_array = []
    flag = True

    while flag:
        chunk = []
        for _ in range(chunk_size):
            try:
                number = next(numbers_generator)
                chunk.append(number)

            except StopIteration:
                flag = False
                break

        if not flag:
            break

        processed_chunk = process_chunk(chunk)
        processed_array.extend(processed_chunk)
        print(processed_array)


if __name__ == '__main__':
    process()

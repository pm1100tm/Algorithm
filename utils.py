import time


def prvalue(print_time: bool = False, print_result=False):
    def decortor(func):
        def wrapper(*args, **kwargs):
            time_s = time.time()
            result = func(*args, **kwargs)
            time_e = time.time()

            if print_result:
                print(f"{result=}")

            if print_time:
                print(
                    f"Function {func.__name__} "
                    f"took {time_e - time_s:.10f} seconds to execute\n"
                )

            return result

        return wrapper

    return decortor


class CommonUtils:

    @staticmethod
    def logging_time(original_fn):
        def wrapper_fn(*args, **kwargs):
            start_time = time.time()
            result     = original_fn(*args, **kwargs)
            end_time   = time.time()

            print('Working Time[{}]: {} sec'. format(
                    original_fn.__name__,
                    end_time - start_time
                )
            )

            return result

        return wrapper_fn

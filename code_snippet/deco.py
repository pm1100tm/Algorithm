import time
import functools


def deco_calculate_time(func):
    """
    데코레이터: 시간 측정
    """

    def wrapper(*args, **kwargs):
        t1 = time.time()
        ret = func(*args, **kwargs)
        t2 = time.time()
        execution_time = t2 - t1
        print(f"Func[{func.__name__}] execution time: {execution_time:.8f} seconds")

        return ret

    return wrapper


def deco_sample_for_with_param(param1: int = 0, param2: bool = True):
    """
    데코레이터: 파라미터를 받아 처리하는 데코레이터 샘플
    """

    def decorator(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # some operations
            print(f'***{func.__name__} start')
            print(param1, param2, args, kwargs)
            result = func(*args, *kwargs)
            print(f'result: {result}')
            print(f'***{func.__name__} end')

            return result
        return wrapper
    return decorator


if __name__ == '__main__':
    @deco_calculate_time
    def make_a_to_z() -> list[str]:
        a_to_z = []
        for n in range(26):
            a_to_z.append(chr(ord('a') + n))

        return a_to_z

    make_a_to_z()

    print('---------------------------------------------------------------------------')

    @deco_sample_for_with_param()
    def sample(a: int, b: int):
        return a + b

    sample(1, 2)

    print('---------------------------------------------------------------------------')

    def my_decorator(func):
        # @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """Wrapper function."""
            print("Something is happening before the function is called.")
            result = func(*args, **kwargs)
            print("Something is happening after the function is called.")
            return result

        return wrapper

    @my_decorator
    def say_hello():
        """This function says hello."""
        print("Hello!")

    say_hello()
    print(say_hello.__name__) # 출력: wrapper
    print(say_hello.__doc__) # 출력: Wrapper function

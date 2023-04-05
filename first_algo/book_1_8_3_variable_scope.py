x = 10


def update1():
    """
    여기서의 x 는 지역변수로 인식된다.
    x 는 전역변수로 선언되어있고, 전역변수는 읽기만 가능하기 때문에 에러가 발생한다.
    """
    x += 1 # error
    print(x)


def update2():
    """
    전역변수를 수정하는 방버은 global 키워드를
    """
    global x
    x += 1
    print(x)


if __name__ == '__main__':
    try:
        update1()
    except UnboundLocalError as e:
        print(f"{e.__class__.__name__}: {e}")

    update2()

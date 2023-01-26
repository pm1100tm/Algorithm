from first_algo.mylogger import logger


def _add(a: int, b: int, a_list: list):
    """
    먼저 매개변수와 인수의 차이에 대해서 알고 넘어가자.
    # 매개변수: 함수의 인자로 전달된 값을 받는 변수(변수라는 것이 중요 포인트)
    # 인수: 함수를 호출할 때 전달하는 입력 값
    # def _add(a, b): -> a, b 는 매개변수, _add(1, 2) -> 1, 2 는 인수
    * important: 매개변수는 함수를 정의, 인수는 함수를 호출할 때

    여기서 파라미터 a 는 인수 x 의 값을 복사해서 온다.
    param a 의 주소 값과, 인수 x 의 주소 값을 보면 같다는 것을 알 수 있다.
    *파이썬에서 모든 것은 객체로 취급되기 때문이다.
    그런데 여기서 주의해야 할 것은, 파라미터와 인수는 자료형에 따라서 다르게 동작한다는 점이다.
    예를들면, a 에 다른 값을 대입한다면 x 의 값도 바뀔 것이라고 생각한다는 것인데,
    x 의 값은 변하지 않는다.
    어디까지나 param a 는 인수 x 를 복사해온 것이기 때문이며, 함수 안에서 다른 값을 대입했을 때는
    재정의 된다. 그러나 int 자료형 말고 list 를 보자.
    인수 x_list 를 넘기고 param a_list 는 복사되어 온다. 그 후 a_list 의 값 추가하면,
    x_list 도 동일하게 변경되어있다.

    함수에서 고쳐쓸 수 없는 자료형은 정수와 부동소수점 숫자, 문자열, 튜플 등이다.
    이러한 자료형을 immutable type 이라고 한다.
    반면, list, dict, set 과 같은 자료형은 함수에서 고쳐 쓸 수 있음으로 가변현 mutable type 이라고 한다.
    * important: 따라서, 파이썬에서 함수에 인수를 전달할 때는 해당 인수가 불변형인지 가변형인지 의식해서
      구별해서 써야한다.

    """
    logger.info("***start _add function")
    assert isinstance(a, int) and isinstance(b, int), f"Type error, {a} or {b} it not int"
    assert isinstance(a_list, list), f"Type error, {c} it not list"

    logger.info(f"id - a: {id(a)}")
    logger.info(f"id - x: {id(x)}")
    logger.info(f"a: {a}")
    logger.info(f"x: {x}")

    a = 2

    logger.info(f"a: {a}")
    logger.info(f"x: {x}")

    a_list.append(3)
    logger.info(f"c_list: {a_list}")
    logger.info(f"x_list: {x_list}")


if __name__ == '__main__':
    x = 1
    y = 2
    x_list = [1, 2]
    _add(x, y, x_list)
    logger.info("***end _add function")

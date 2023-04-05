class User:
    """
    _ 로 시작하는 변수와 메서드는 외부에서 참조하지 않는다는 규칙이 있음.
    __ 로 시작하는 변수나 메서드에 접근하면 오류 발생
    """

    def __init__(self, name: str, password: str, age: int):
        self._name = name
        self.__password = password
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, pw: str):
        if not isinstance(pw, str):
            raise ValueError("pw type is wrong")

        self.__password = pw


if __name__ == '__main__':
    user = User("python", "1234", 10)
    print(user.name)
    try:
        user.name = "python3"
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")

    user._name = "python3"
    print(user._name)

    try:
        print(user.__password)
    except AttributeError as e:
        print(f"{e.__class__.__name__}: {e}")

    print(user.password)
    user.password = "12345"
    print(user.password)

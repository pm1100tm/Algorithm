"""
A씨는 두 개의 버전을 비교하는 프로그램을 작성해야 한다. 버전은 다음처럼 "." 으로 구분된 문자열이다.
버전 예) 1.0.0, 1.0.23, 1.1

두 개의 버전을 비교하는 프로그램을 작성하시오.
다음은 버전 비교의 예이다.

0.0.2 > 0.0.1
1.0.10 > 1.0.3
1.2.0 > 1.1.99
1.1 > 1.0.1
"""


def custom_zfill(x_value, max):
    """
    Convert string x_value to int value with zero attached right side
    as many as max number.
    :param x_value: (string)
    :param max: (int)
    :return: (int)
    """
    return int("{x:0<{m}}" .format(x=x_value, m=max))


def compare_version(ver1, ver2):
    """
    Compare ver1 with ver2 so that return the follow way.
    Return 1, ver1 is greater than ver2. In other case, return -1.
    Return 0, ver1 is equal with ver2.
    :param ver1: (string) version info
    :param ver2: (string) version info
    :return: -1, 0, 1
    """
    ver1 = ver1.split(".")
    ver2 = ver2.split(".")
    if len(ver1) < 3: ver1.append("0")
    if len(ver2) < 3: ver2.append("0")
    result = 0

    for i in range(0, 3):
        # print("i:", str(i))
        if int(ver1[i]) == int(ver2[i]):
            continue
        else:
            max_len = 0
            if len(ver1[i]) != len(ver2[i]):
                if len(ver1[i]) > len(ver2[i]):
                    max_len = len(ver1[i])
                else:
                    max_len = len(ver2[i])

            if custom_zfill(ver1[i], max_len) == custom_zfill(ver2[i], max_len):
                result = 0
                break
            else:
                if custom_zfill(ver1[i], max_len) > custom_zfill(ver2[i], max_len):
                    result = 1
                    break
                else:
                    result = -1
                    break

    return result


case1 = ["0.1.20", "0.1.2"] # OK
case2 = ["1.0.20", "0.1.2"] # OK
case3 = ["1.2.20", "0.1.2"] # OK
case4 = ["1.1", "0.1.2"] # OK
case5 = ["01.1.20", "10.1.2"] # OK
case6 = ["1.2.099", "01.02.99"] # OK
case7 = ["1.2.098", "0.2.1"] # OK
case8 = ["1.1.0", "1.01"] # OK
case_list = [case1, case2, case3, case4, case5, case6, case7, case8,]

for i in case_list:
    if compare_version(i[0], i[1]) == 0:
        print("{0} == {1}" .format(i[0], i[1]))
    elif compare_version(i[0], i[1]) > 0:
        print("{0} > {1}" .format(i[0], i[1]))
    else:
        print("{0} < {1}" .format(i[0], i[1]))
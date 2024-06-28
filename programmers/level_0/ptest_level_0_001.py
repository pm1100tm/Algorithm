from .level_0_001_나이계산 import solution

import pytest


@pytest.fixture
def data_level_0_001_001():
    return -1


@pytest.fixture
def data_level_0_001_002():
    return 121


@pytest.fixture
def data_level_0_001_003() -> tuple[int, int]:
    param, result = 40, 1983
    return param, result


@pytest.fixture
def data_level_0_001_004() -> tuple[int, int]:
    param, result = 23, 2000
    return param, result


def test_level_0_001_error_case_001(data_level_0_001_001):
    with pytest.raises(ValueError) as e:
        solution(data_level_0_001_001)

    print(f"\n{str(e)}")


def test_level_0_001_error_case_002(data_level_0_001_002):
    with pytest.raises(ValueError) as e:
        solution(data_level_0_001_002)

    print(f"\n{str(e)}")


def test_level_0_001_success_case_001(data_level_0_001_003):
    param, result = data_level_0_001_003[0], data_level_0_001_003[1]

    res = solution(param)
    assert isinstance(res, int)
    assert res == result


def test_level_0_001_success_case_002(data_level_0_001_004):
    param, result = data_level_0_001_004[0], data_level_0_001_004[1]

    res = solution(param)
    assert isinstance(res, int)
    assert res == result

import pytest

from .level_0_002 import solution001, solution002


@pytest.fixture
def data_level_0_002_001():
    return 3, 2, 1500


@pytest.fixture
def data_level_0_002_002():
    return 7, 3, 2333


@pytest.fixture
def data_level_0_002_003():
    return 1, 16, 62


def test_level_0_002_case_001(data_level_0_002_001):
    num1, num2, result = data_level_0_002_001
    assert result == solution001(num1, num2)


def test_level_0_002_case_002(data_level_0_002_002):
    num1, num2, result = data_level_0_002_002
    assert result == solution001(num1, num2)


def test_level_0_002_case_003(data_level_0_002_003):
    num1, num2, result = data_level_0_002_003
    assert result == solution001(num1, num2)


@pytest.mark.parametrize(
    "num1, num2, result", [
        (3, 2, 1500),
        (7, 3, 2333),
        (1, 16, 62),
    ]
)
def test_level_0_002_all_success_case(num1, num2, result):
    assert result == solution001(num1, num2)


@pytest.mark.parametrize(
    "num1, num2, result", [
        (3, 2, 1500),
        (7, 3, 2333),
        (1, 16, 62),
    ]
)
def test_level_0_002_all_success_case_extra(num1, num2, result):
    assert result == solution002(num1, num2)

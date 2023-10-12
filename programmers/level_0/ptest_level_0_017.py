import pytest

from .level_0_017 import solution001, solution002, solution003


@pytest.mark.parametrize(
    "my_string, letter, result", [
        (
            "abcdef", "f", "abcde"
        ),
        (
            "BCBdbe", "B", "Cdbe",
        ),
    ]
)
def test_level_0_017_solution001(my_string, letter, result):
    assert result == solution001(my_string, letter)


@pytest.mark.parametrize(
    "my_string, letter, result", [
        (
            "abcdef", "f", "abcde"
        ),
        (
            "BCBdbe", "B", "Cdbe",
        ),
    ]
)
def test_level_0_017_solution002(my_string, letter, result):
    assert result == solution002(my_string, letter)


@pytest.mark.parametrize(
    "my_string, letter, result", [
        (
            "abcdef", "f", "abcde"
        ),
        (
            "BCBdbe", "B", "Cdbe",
        ),
    ]
)
def test_level_0_017_solution003(my_string, letter, result):
    assert result == solution003(my_string, letter)

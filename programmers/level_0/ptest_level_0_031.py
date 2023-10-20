import pytest

from .level_0_031 import (
    solution,
    solution001,
    solution002,
)


@pytest.mark.parametrize(
    "n, result", [
        (
            0, 0,
        ),
        (
            1, 1,
        ),
        (
            10, 1,
        ),
    ]
)
def test_level_0_031_solution(n, result):
    assert result == solution(n)


@pytest.mark.parametrize(
    "n, result", [
        (
            20, 6
        ),
        (
            100, 9
        ),
    ]
)
def test_level_0_021_solution002(n, result):
    assert result == solution002(n)


@pytest.mark.parametrize(
    "n, result", [
        (
            20, 6
        ),
        (
            100, 9
        ),
    ]
)
def test_level_0_021_solution003(n, result):
    assert result == solution003(n)


@pytest.mark.parametrize(
    "n, result", [
        (
            20, 6
        ),
        (
            100, 9
        ),
    ]
)
def test_level_0_021_solution004(n, result):
    assert result == solution004(n)

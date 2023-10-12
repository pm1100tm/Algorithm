import pytest

from .level_0_019 import (
    solution001,
    solution002,
    solution003,
    solution004,
)


@pytest.mark.parametrize(
    "num_list, result", [
        ([1, 2, 3, 4, 5], [2, 3],),
        ([1, 3, 5, 7], [0, 4],),
    ]
)
def test_level_0_019_solution001(num_list, result):
    assert result == solution001(num_list)


@pytest.mark.parametrize(
    "num_list, result", [
        ([1, 2, 3, 4, 5], [2, 3],),
        ([1, 3, 5, 7], [0, 4],),
    ]
)
def test_level_0_019_solution002(num_list, result):
    assert result == solution002(num_list)


@pytest.mark.parametrize(
    "num_list, result", [
        ([1, 2, 3, 4, 5], [2, 3],),
        ([1, 3, 5, 7], [0, 4],),
    ]
)
def test_level_0_019_solution003(num_list, result):
    assert result == solution003(num_list)


@pytest.mark.parametrize(
    "num_list, result", [
        ([1, 2, 3, 4, 5], [2, 3],),
        ([1, 3, 5, 7], [0, 4],),
    ]
)
def test_level_0_019_solution004(num_list, result):
    assert result == solution004(num_list)

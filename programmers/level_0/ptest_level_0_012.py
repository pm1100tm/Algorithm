import pytest

from .level_0_012 import solution001, solution002


@pytest.mark.parametrize(
    "num_list, result", [
        (
            [1, 2, 3, 4, 5]
            ,[5, 4, 3, 2, 1]
        ),
        (
            [1, 1, 1, 1, 1, 2]
            ,[2, 1, 1, 1, 1, 1]
        ),
        (
            [1, 0, 1, 1, 1, 3, 5]
            ,[5, 3, 1, 1, 1, 0, 1]
        ),
    ]
)
def test_level_0_012_solution001(num_list, result):
    assert result == solution001(num_list)


@pytest.mark.parametrize(
    "num_list, result", [
        (
            [1, 2, 3, 4, 5]
            ,[5, 4, 3, 2, 1]
        ),
        (
            [1, 1, 1, 1, 1, 2]
            ,[2, 1, 1, 1, 1, 1]
        ),
        (
            [1, 0, 1, 1, 1, 3, 5]
            ,[5, 3, 1, 1, 1, 0, 1]
        ),
    ]
)
def test_level_0_012_solution002(num_list, result):
    assert result == solution002(num_list)

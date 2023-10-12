import pytest

from .level_0_015 import solution001, solution002


@pytest.mark.parametrize(
    "array, height, result", [
        (
            [149, 180, 192, 170]
            , 167, 3
        ),
        (
            [180, 120, 140]
            , 190, 0
        ),
        (
            [189]
            , 190, 0
        ),
    ]
)
def test_level_0_015_solution001(array, height, result):
    assert result == solution001(array, height)


@pytest.mark.parametrize(
    "array, height, result", [
        (
            [149, 180, 192, 170]
            , 167, 3
        ),
        (
            [180, 120, 140]
            , 190, 0
        ),
        (
            [189]
            , 190, 0
        ),
    ]
)
def test_level_0_015_solution002(array, height, result):
    assert result == solution002(array, height)

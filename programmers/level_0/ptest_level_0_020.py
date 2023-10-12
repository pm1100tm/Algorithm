import pytest

from .level_0_020 import solution001


@pytest.mark.parametrize(
    "sides, result", [
        (
            [1, 2, 3]
            , 2
        ),
        (
            [3, 6, 2]
            , 2
        ),
        (
            [199, 72, 222]
            , 1
        ),
    ]
)
def test_level_0_020_solution001(sides, result):
    assert result == solution001(sides)

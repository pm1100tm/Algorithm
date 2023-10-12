import pytest

from .level_0_007 import solution


@pytest.mark.parametrize(
    "angle, result", [
        (0,  1),
        (1,  1),
        (89, 1),
        (90, 2),
        (91, 3),
        (179, 3),
        (180, 4),
        (181, 4),
        (269, 4),
        (270, 4),
        (271, 4),
        (359, 4),
        (360, 4),
        (361, 4),
    ]
)
def test_level_0_007_case(angle, result):
    assert result == solution(angle)

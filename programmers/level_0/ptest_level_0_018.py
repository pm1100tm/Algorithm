import pytest

from .level_0_018 import solution001, solution002


@pytest.mark.parametrize(
    "dot, result", [
        (
            [2, 4], 1,
        ),
        (
            [-7, 9], 2,
        ),
    ]
)
def test_level_0_018_solution001(dot, result):
    assert result == solution001(dot)


@pytest.mark.parametrize(
    "dot, result", [
        (
            [2, 4], 1,
        ),
        (
            [-7, 9], 2,
        ),
    ]
)
def test_level_0_018_solution002(dot, result):
    assert result == solution002(dot)

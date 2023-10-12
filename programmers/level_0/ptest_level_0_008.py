import pytest

from .level_0_008 import solution001, solution002


@pytest.mark.parametrize(
    "n, result", [
        (10,  30),
        (4,  6),
    ]
)
def test_level_0_008_success_case_001(n, result):
    assert result == solution001(n)


@pytest.mark.parametrize(
    "n, result", [
        (10,  30),
        (4,  6),
    ]
)
def test_level_0_008_success_case_002(n, result):
    assert result == solution002(n)

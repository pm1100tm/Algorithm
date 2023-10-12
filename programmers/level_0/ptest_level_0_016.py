import pytest

from .level_0_016 import solution001, solution002


@pytest.mark.parametrize(
    "strlist, result", [
        (
            ["We", "are", "the", "world!"]
            , [2, 3, 3, 6]
        ),
        (
            ["I", "Love", "Programmers."]
            , [1, 4, 12]
        ),
    ]
)
def test_level_0_016_solution001(strlist, result):
    assert result == solution001(strlist)


@pytest.mark.parametrize(
    "strlist, result", [
        (
                ["We", "are", "the", "world!"]
                , [2, 3, 3, 6]
        ),
        (
                ["I", "Love", "Programmers."]
                , [1, 4, 12]
        ),
    ]
)
def test_level_0_016_solution002(strlist, result):
    assert result == solution002(strlist)

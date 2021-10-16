import pytest

@pytest.fixture
def test_date_001():
    return {
        'nums'    : [2, 7, 11, 15],
        'target'  : 13,
        'expected': (0, 2)
    }

@pytest.fixture
def test_date_002():
    return {
        'nums'    : [2, 7, 11, 15],
        'target'  : 9,
        'expected': (0, 1)
    }

@pytest.fixture
def test_date_003():
    return {
        'nums'    : [2, 7, 11, 15],
        'target'  : 26,
        'expected': (2, 3)
    }

@pytest.fixture
def test_date_004():
    return {
        'nums'    : [2, 7, 11, 15],
        'target'  : 100,
        'expected': (0, 0)
    }

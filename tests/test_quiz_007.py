from algorithm_interview.quiz_007 import TargetIndex


def test_solution_001(test_date_001):
    result = TargetIndex.my_solution_one(
        test_date_001['nums'], test_date_001['target']
    )

    assert result == test_date_001['expected']

def test_solution_002(test_date_002):
    result = TargetIndex.my_solution_one(
        test_date_002['nums'], test_date_002['target']
    )

    assert result == test_date_002['expected']

import unittest
import traceback
from utils import CommonUtils


class Solution:
    """ 문자열 다루기 기본
        문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요.
        예를 들어 s가 a234이면 False를 리턴하고 1234라면 True를 리턴하면 됩니다.
        
        제한 사항
            s는 길이 1 이상, 길이 8 이하인 문자열입니다.
        
        입출력 예
            a234    false
            1234    true
        
        위의 문제에 대한 솔루션 메서드를 1개 이상 작성하기
    """
    
    @CommonUtils.logging_time
    def my_solution(self, s: str) -> bool:
        if len(s) == 4 or len(s) == 6:
            
            if s.isdigit():
                return True
        
        return False
    
    @CommonUtils.logging_time
    def solution_one(self, s: str) -> bool:
        return s.isdigit() and len(s) in (4, 6)

    @CommonUtils.logging_time
    def solution_two(self, s: str) -> bool:
        import re
        return bool(re.match("^(\d{4}|\d{6})$", s))

    @CommonUtils.logging_time
    def solution_three(self, s: str) -> bool:
        try:
            int(s)
        except ValueError as e:
            traceback.print_exc(e)
            return False
        
        except TypeError as e:
            traceback.print_exc(e)
            return False
        
        return len(s) == 4 or len(s) == 6


class TestSolution(unittest.TestCase):
    
    def setUp(self) -> None:
        self.solution = Solution()
        self.case_001 = '1234'
        self.case_002 = 'a123'
        self.case_003 = '123456'
        self.case_004 = '12b3a4'

        self.expect_list = [True, False, True, False]
        
    def test_my_solution(self):
        case_result_list = [
            self.solution.my_solution(self.case_001),
            self.solution.my_solution(self.case_002),
            self.solution.my_solution(self.case_003),
            self.solution.my_solution(self.case_004)
        ]
        
        for index, result in enumerate(case_result_list):
            self.assertEqual(
                self.expect_list[index],
                result
            )
    
    def test_solution_one(self):
        case_result_list = [
            self.solution.solution_one(self.case_001),
            self.solution.solution_one(self.case_002),
            self.solution.solution_one(self.case_003),
            self.solution.solution_one(self.case_004)
        ]
        
        for index, result in enumerate(case_result_list):
            self.assertEqual(
                self.expect_list[index],
                result
            )

    def test_solution_two(self):
        case_result_list = [
            self.solution.solution_two(self.case_001),
            self.solution.solution_two(self.case_002),
            self.solution.solution_two(self.case_003),
            self.solution.solution_two(self.case_004)
        ]
        
        for index, result in enumerate(case_result_list):
            self.assertEqual(
                self.expect_list[index],
                result
            )


if __name__ == "__main__":
    unittest.main()

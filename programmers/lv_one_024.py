import unittest


class Solution:
    """ 문자열을 정수로 바꾸기
    문자열 s를 숫자로 변환한 결과를 반환하는 함수, solution을 완성하세요.

    제한 조건
        s의 길이는 1 이상 5이하입니다.
        s의 맨앞에는 부호(+, -)가 올 수 있습니다.
        s는 부호와 숫자로만 이루어져있습니다.
        s는 0으로 시작하지 않습니다.
        
    입출력 예
        예를들어 str이 1234이면 1234를 반환하고, -1234이면 -1234를 반환하면 됩니다.
        str은 부호(+,-)와 숫자로만 구성되어 있고, 잘못된 값이 입력되는 경우는 없습니다.
    """
    
    def my_solution(self, s: str) -> int:
        return int(s)


class TestSolution(unittest.TestCase):
    
    def setUp(self) -> None:
        self.solution = Solution()
        
        self.case_one   = '-1'
        self.case_two   = '-12345'
        self.case_three = '54321'
        self.case_four  = '321'
        self.case_five  = '-321'
        
        self.case_result_one   = -1
        self.case_result_two   = -12345
        self.case_result_three = 54321
        self.case_result_four  = 321
        self.case_result_five  = -321
    
    def test_my_solution(self):
        result_one = self.solution.my_solution(self.case_one)
        
        self.assertEqual(
            result_one,
            self.case_result_one,
        )

        result_two = self.solution.my_solution(self.case_two)

        self.assertEqual(
            result_two,
            self.case_result_two,
        )

        result_three = self.solution.my_solution(self.case_three)
        
        self.assertEqual(
            result_three,
            self.case_result_three,
        )
        
        result_four = self.solution.my_solution(self.case_four)
        
        self.assertEqual(
            result_four,
            self.case_result_four,
        )
        
        result_five = self.solution.my_solution(self.case_five)
        
        self.assertEqual(
            result_five,
            self.case_result_five,
        )


if __name__ == "__main__":
    unittest.main()

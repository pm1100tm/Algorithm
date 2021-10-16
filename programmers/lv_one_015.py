import unittest

from utils import CommonUtils


class Solution:
    """ 문자열 내림차순으로 배치하기
    문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴하는 함수, solution을 완성해주세요.
    s는 영문 대소문자로만 구성되어 있으며, 대문자는 소문자보다 작은 것으로 간주합니다.

    제한 사항
        str은 길이 1 이상인 문자열입니다.
    
    입출력 예
        s: "Zbcdefg"
        return : "gfedcbZ"
    """
    
    def my_solution(self, s: str) -> str:
        
        if not s.isalpha():
            return ""
        
        return ''.join(sorted(s)[::-1])


class TestSolution(unittest.TestCase):
    
    def setUp(self) -> None:
        self.solution = Solution()
        
        self.case_one = "Zbcdefg"
        self.case_two = "abcdabcdA"
        
        self.case_one_result = "gfedcbZ"
        self.case_two_result = "ddccbbaaA"

    @CommonUtils.logging_time
    def test_my_solution(self):
        result_one = self.solution.my_solution(self.case_one)
        
        self.assertEqual(
            self.case_one_result,
            result_one
        )
        
        result_two = self.solution.my_solution(self.case_two)
        
        self.assertEqual(
            self.case_two_result,
            result_two
        )

        
if __name__ == "__main__":
    unittest.main()

import unittest
from utils import CommonUtils


class Solution:
    """ 가운데 글자 가져오기
    단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요.
    단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.
    
    재한사항
        s는 길이가 1 이상, 100이하인 스트링입니다.
        
    입출력
        abcde   c
        qwer    we
    """
    
    def my_solution(self, s: str) -> str:
        index_num = int(len(s)/2)
        
        if len(s) % 2 != 0:
            return s[index_num:index_num + 1]
        
        return s[index_num - 1:index_num + 1]
    
    def best_solution_i_think(self, s: str) -> str:
        return s[(len(s) - 1)//2 : len(s) // 2 + 1]


class TestSolution(unittest.TestCase):
    
    def setUp(self) -> None:
        self.solution = Solution()
        
        self.case_list = [
            'abcde',
            'qwer',
            'a',
            'ab',
            '11111111112222222222333333333344444444445555555555'
            '66666666667777777777888888888899999999990000000000'
        ]
        
        self.case_result = [
            "c",
            "we",
            "a",
            "ab",
            "56"
        ]
    
    @CommonUtils.logging_time
    def test_my_solution(self):
        
        for i in range(len(self.case_list)):
            self.assertEqual(
                self.case_result[i],
                self.solution.my_solution(self.case_list[i])
            )
    
    @CommonUtils.logging_time
    def test_best_solution_i_think(self):
        
        for i in range(len(self.case_list)):
            self.assertEqual(
                self.case_result[i],
                self.solution.best_solution_i_think(self.case_list[i])
            )


if __name__ == '__main__':
    unittest.main()
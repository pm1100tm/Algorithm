import unittest

from utils import CommonUtils


class Solution:
    """ 이상한 문자 만들기
    문자열 s는 한 개 이상의 단어로 구성되어 있습니다.
    각 단어는 하나 이상의 공백문자로 구분되어 있습니다.
    각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution 을 완성하세요.
    
    제한 사항
        문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.
        첫 번째 글자는 0번째 인덱스로 보아 짝수번째 알파벳으로 처리해야 합니다.
    
    s                   return
    'try hello world'   'TrY HeLlO WoRlD'
    """
    
    def my_solution(self, string: str) -> str:
        answer = [''] * (string.count(' ') + 1)
        chunk_list = list(map(str, string.split(' ')))
        
        for i, chunk in enumerate(chunk_list):
            
            for j, char in enumerate(chunk):
                
                if j % 2 == 0:
                    answer[i] += char.upper()
                    continue
                
                answer[i] += char.lower()
        
        return ' '.join(answer)
    
    def other_solution_one(self, string: str) -> str:
        res = []
        
        for x in string.split(' '):
            
            word = ''
            
            for i in range(len(x)):
                c = x[i].upper() if i % 2 == 0 else x[i].lower()
                word = word + c
                
            res.append(word)
            
        return ' '.join(res)
    

class TestClass(unittest.TestCase):
    
    def setUp(self) -> None:
        self.solution = Solution()
        
        self.case_one        = 'try hello world'
        self.case_one_result = 'TrY HeLlO WoRlD'
    
    @CommonUtils.logging_time
    def test_my_solution_one(self):
        
        result = self.solution.my_solution(self.case_one)
        
        self.assertEqual(
            self.case_one_result,
            result
        )


if __name__ == '__main__':
    unittest.main()

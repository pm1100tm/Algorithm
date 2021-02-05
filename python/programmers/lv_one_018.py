import unittest


class Solution:
    """ 3진법 뒤집기
    자연수 n이 매개변수로 주어집니다.
    n을 3진법 상에서 앞뒤로 뒤집은 후,
    이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.
    
    제한 사항
        n은 1 이상 100,000,000 이하인 자연수입니다.
        
    n   result
    45  7
    125 229
    
    입출력 예 설명
        입출력 예 #1 답을 도출하는 과정은 다음과 같습니다.
    
    n (10진법)   n (3진법)    앞뒤 반전(3진법)  10진법으로 표현
    45          1200        0021            7
    125         11122       22111           229
    """
    
    def my_solution(self, n: int) -> int:
        """ reference
        *https://programmers.co.kr/learn/courses/4008/lessons/12733
        *https://wlstyql.tistory.com/41
        """
        base_three = ''
        
        while n > 0:
            n, mod = divmod(n, 3)
            base_three += str(mod)
        
        answer = 0
        
        for idx, value in enumerate(base_three[::-1]):
            answer += int(value) * (3 ** idx)
        
        return answer
    
    def best_solution_i_think(self, n: int) -> int:
        temp = ''
        
        while n:
            temp += str(n % 3)
            n = n // 3
        
        answer = int(temp, 3)
        return answer


class TestSolution(unittest.TestCase):
    
    def setUp(self) -> None:
        self.solution = Solution()
        
        self.case_list        = [45, 125]
        self.case_result_list = [7 , 229]
    
    def test_my_solution(self):
        
        for index, case in enumerate(self.case_list):
            self.assertEqual(
                self.case_result_list[index],
                self.solution.my_solution(case)
            )


if __name__ == '__main__':
    unittest.main()

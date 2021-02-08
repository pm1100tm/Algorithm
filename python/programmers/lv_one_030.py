import unittest


class Solution:
    """ 정수 내림차순으로 배치하기
    함수 solution 은 정수 n을 매개변수로 입력받습니다.
    n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요.
    예를들어 n이 118372면 873211을 리턴하면 됩니다.
    
    제한 조건
        n은 1이상 8000000000 이하인 자연수입니다.
    
    입출력 예
        n       return
        118372  873211
    """
    
    def my_solution(self, n: int) -> int:
        sorted_number = map(str, sorted(str(n), reverse=True))
        answer = int(''.join(sorted_number))
        
        return answer
    
    def best_solution_i_think(self, n: int) -> int:
        return int(''.join(sorted(str(n), reverse=True)))
    
    def other_solution_one(self, n: int) -> int:
        ls = list(str(n))
        ls.sort(reverse=True)
        
        return int("".join(ls))


class TestSolution(unittest.TestCase):
    
    def setUp(self) -> None:
        self.solution = Solution()
        
        self.case = [
            118372,
            118370
        ]
        
        self.result = [
            873211,
            873110,
        ]
    
    def test_my_solution(self):
        for index, case in enumerate(self.case):
            
            result = self.solution.my_solution(case)
            
            self.assertEqual(
                self.result[index],
                result
            )
    
    def test_best_solution_i_think(self):
        for index, case in enumerate(self.case):
            result = self.solution.best_solution_i_think(case)
            
            self.assertEqual(
                self.result[index],
                result
            )


if __name__ == '__main__':
    unittest.main()

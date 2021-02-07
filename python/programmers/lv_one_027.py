class Solution:
    """ 자릿수 더하기
    자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
    예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.
    
    제한사항
        N의 범위 : 100,000,000 이하의 자연수
    
    입출력 예
        N       answer
        123     6
        987     24
    """
    
    def my_solution(self, n: int) -> int:
        if n < 10:
            return n
        
        answer = 0
        
        for i in range(str(n)):
            answer += int(i)
        
        return answer
    
    def best_solution_i_think(self, n: int) -> int:
        if n < 10:
            return n
        
        return (n % 10) + self.best_solution_i_think(n // 10)
    
    def other_solution_one(self, n: int) -> int:
        return sum(map(int, str(n)))

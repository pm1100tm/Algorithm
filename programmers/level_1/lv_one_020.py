from typing import List


class Solution:
    """ 체육복
    점심시간에 도둑이 들어, 일부 학생이 체육복을 도난당했습니다.
    다행히 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다.
    학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다.
    예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다.
    체육복이 없으면 수업을 들을 수 없기 때문에 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 합니다.
    
    전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost,
    여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때,
    체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.
    
    제한사항
        전체 학생의 수는 2명 이상 30명 이하입니다.
        체육복을 도난당한 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
        여벌의 체육복을 가져온 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
        여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있습니다.
        여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다.
        이때 이 학생은 체육복을 하나만 도난당했다고 가정하며,
        남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.
    
    입출력 예
        n   lost    reserve	    return
        5   [2, 4]  [1, 3, 5]   5
        5   [2, 4]  [3]	        4
        3   [3]     [1]         2
    """
    
    def my_solution(self, n: int, lost: List[int], reserve: List[int]) -> int:
        """ 런타임 에러 16.7점
        """
        max_num = n - len(lost)
        
        for v in lost:
            if v in reserve:
                reserve.remove(v)
        
        for r in reserve:
            if r-1 in lost:
                lost.remove(r + 1)
                max_num += 1
            elif r+1 in lost:
                lost.remove(r + 1)
                max_num += 1
        
        return max_num
    
    def my_solution_two(self, n: int, lost: List[int], reserve: List[int]) -> int:
        """ 75.0점
        """
        max_num = n - len(lost)
        count = 0
        
        for r in reserve:
            temp = max_num
            if r-1 in lost:
                count += 1
                max_num += 1
            
            if temp == max_num and r+1 in lost:
                count += 1
                max_num += 1
            
            if count == len(lost):
                break
        
        return max_num
    
    def other_solution_one(self, n: int, lost: List[int], reserve: List[int]) -> int:
        """ 참고자료
        https://www.youtube.com/watch?v=9mgXd5WUp8U
        """
        answer = [1] * n
        
        for i in reserve:
            answer[i-1] = 2
        
        for i in lost:
            answer[i-1] = answer[i-1] - 1
        
        for i, v in enumerate(answer):
            if i > 0 and v == 0 and answer[i-1] == 2:
                answer[i] = 1
                answer[i-1] = 1
            elif i < n-1 and v == 0 and answer[i+1] == 2:
                answer[i] = 1
                answer[i+1] = 1
        
        return n - answer.count(0)
    
    def other_solution_two(self, n: int, lost: List[int], reserve: List[int]) -> int:
        _reserve = [r for r in reserve if r not in lost]
        _lost = [l for l in lost if l not in reserve]
        
        for r in _reserve:
            f = r - 1
            b = r + 1
            
            if f in _lost:
                _lost.remove(f)
            
            elif b in _lost:
                _lost.remove(b)
        
        return n - len(_lost)

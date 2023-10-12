from typing import List


class Solution:
    """ 제일 작은 수 제거하기
    정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수, solution 을 완성해주세요.
    단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요.
    예를들어 arr 이 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고, [10]면 [-1]을 리턴 합니다.
    
    제한 조건
        arr 은 길이 1 이상인 배열입니다.
        인덱스 i, j에 대해 i ≠ j이면 arr[i] ≠ arr[j] 입니다.
    
    입출력 예
        arr	        return
        [4,3,2,1]   [4,3,2]
        [10]        [-1]
    """
    
    def my_solution(self, arr: List[int]) -> object:
        if not arr or len(arr) == 1:
            return [-1]
        
        min_num = min(arr)
        arr.remove(min_num)
        
        return arr
    
    def best_solution_i_think(self, arr: List[int]) -> object:
        if len(arr) == 1 or not arr:
            return [-1]
        
        return [num for num in arr if num > min(arr)]
"""
타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴


"""
from typing import List


class TargetIndex:
    
    def my_solution(self, number_list: List[int], target_number: int) -> (int, int):
        a = 0
        b = 0
        for i, number in enumerate(number_list):
            n = target_number - number
            
            if n in number_list[i+1:]:
                a = i
                b = number_list.index(n)
        
        return a, b


if __name__ == '__main__':
    nums   = [2, 7, 11, 15]
    target = 9
    
    target_index = TargetIndex()
    
    result = target_index.my_solution(number_list=nums, target_number=target)
    print(result)

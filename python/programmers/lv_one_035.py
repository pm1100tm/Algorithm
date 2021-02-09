import unittest
from typing import List


class Solution:
    """ 키패드 누르기
    이 전화 키패드에서 왼손과 오른손의 엄지손가락만을 이용해서 숫자만을 입력하려고 합니다.
    맨 처음 왼손 엄지손가락은 * 키패드에 오른손 엄지손가락은 # 키패드 위치에서 시작하며, 엄지손가락을 사용하는 규칙은 다음과 같습니다.
    
    1. 엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 키패드 이동 한 칸은 거리로 1에 해당합니다.
    2. 왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지손가락을 사용합니다.
    3. 오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지손가락을 사용합니다.
    4. 가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때는 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용합니다.
    4-1. 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용합니다.
    
    순서대로 누를 번호가 담긴 배열 numbers, 왼손잡이인지 오른손잡이인 지를 나타내는 문자열 hand 가 매개변수로 주어질 때,
    각 번호를 누른 엄지손가락이 왼손인 지 오른손인 지를 나타내는 연속된 문자열 형태로 return 하도록
    solution 함수를 완성해주세요.
    
    [제한사항]
        numbers 배열의 크기는 1 이상 1,000 이하입니다.
        numbers 배열 원소의 값은 0 이상 9 이하인 정수입니다.
        hand 는 "left" 또는 "right" 입니다.
        "left"는 왼손잡이, "right"는 오른손잡이를 의미합니다.
        왼손 엄지손가락을 사용한 경우는 L, 오른손 엄지손가락을 사용한 경우는 R을 순서대로 이어붙여 문자열 형태로 return 해주세요.
        
    입출력 예
        numbers	hand                                    result
        [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]   "right"     "LRLLLRLLRRL"
        [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]   "left"      "LRLLRRLLLRR"
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]      "right"     "LLRLLRLLRL"
    """
    
    def my_solution(self, numbers: List[int], hand: str) -> str:
        position = {
            # left
            1 : (0, 0),
            4 : (1, 0),
            7 : (2, 0),
            
            # right
            3 : (0, 2),
            6 : (1, 2),
            9 : (2, 2),
            
            # middle
            2 : (0, 1),
            5 : (1, 1),
            8 : (2, 1),
            0 : (3, 1)
        }

        lp   = (3, 0)
        rp   = (3, 2)
        
        answer = ''
        
        for n in numbers:
            
            if n == 1 or n == 4 or n == 7:
                answer += 'L'
                lp = position[n]
                continue
            
            if n == 3 or n == 6 or n == 9:
                answer += 'R'
                rp = position[n]
                continue
            
            from_l = abs(position[n][0] - lp[0]) + abs(position[n][1] - lp[1])
            from_r = abs(position[n][0] - rp[0]) + abs(position[n][1] - rp[1])
            
            if from_l == from_r:
                if hand == 'right':
                    answer += 'R'
                    rp = position[n]
                    continue
                
                answer += 'L'
                lp = position[n]
                continue
            
            if from_l > from_r:
                answer += 'R'
                rp = position[n]
                continue
            else:
                answer += 'L'
                lp = position[n]
                continue
        
        return answer


class TestSolution(unittest.TestCase):
    
    def setUp(self) -> None:
        self.solution = Solution()
        
        self.case_one = [
            [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],
            'right'
        ]
        
        self.case_two = [
            [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],
            'left'
        ]
    
        self.case_three = [
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
            'right'
        ]
        
        self.result_one   = "LRLLLRLLRRL"
        self.result_two   = "LRLLRRLLLRR"
        self.result_three = "LLRLLRLLRL"
        
    def test_my_solution_one(self):
        result = self.solution.my_solution(self.case_one[0], self.case_one[1])
        
        self.assertEqual(
            self.result_one,
            result
        )

    def test_my_solution_two(self):
        result = self.solution.my_solution(self.case_two[0], self.case_two[1])
    
        self.assertEqual(
            self.result_two,
            result
        )

    def test_my_solution_three(self):
        result = self.solution.my_solution(self.case_three[0], self.case_three[1])
    
        self.assertEqual(
            self.result_three,
            result
        )


if __name__ == '__main__':
    unittest.main()


import unittest
from collections import Counter, defaultdict
from typing import List

from utils import CommonUtils


class Solution:
    """ 모의고사
    1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때,
    가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.
    
    제한 조건
        시험은 최대 10,000 문제로 구성되어있습니다.
        문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
        가장 높은 점수를 받은 사람이 여럿일 경우, return 하는 값을 오름차순 정렬해주세요.
    
    입출력 예
        [1,2,3,4,5]	[1]
        [1,3,2,4,2]	[1,2,3]
    
    입출력 예 설명
        입출력 예 #1
        - 수포자 1은 모든 문제를 맞혔습니다.
        - 수포자 2는 모든 문제를 틀렸습니다.
        - 수포자 3은 모든 문제를 틀렸습니다.
        따라서 가장 문제를 많이 맞힌 사람은 수포자 1입니다.

    입출력 예 #2
        -모든 사람이 2문제씩을 맞췄습니다.
    """
    
    def my_solution(self, answers: List[int]) -> List[int]:
        student_one   = [1, 2, 3, 4, 5]
        student_two   = [2, 1, 2, 3, 2, 4, 2, 5]
        student_three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
        
        result = defaultdict(int)
        
        for index, value in enumerate(answers):
            if student_one[index % len(student_one)] == value:
                result[1] += 1
            
            if student_two[index % len(student_two)] == value:
                result[2] += 1

            if student_three[index % len(student_three)] == value:
                result[3] += 1
        
        c = Counter(result)
        max_value = max(c.values())
        answer_list = []
        
        for key, value in c.items():
            if value == max_value:
                answer_list.append(key)
        
        answer_list.sort()
        return answer_list
    
    def best_solution_i_think(self, answers: List[int]) -> List[int]:
        student_answers = [
            [1, 2, 3, 4, 5],
            [2, 1, 2, 3, 2, 4, 2, 5],
            [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
        ]
        
        scores = [0] * len(student_answers)
        
        for index, answer in enumerate(answers):
            for idx, student_answer in enumerate(student_answers):
                if student_answer[index % len(student_answer)] == answer:
                    scores[idx] += 1
        
        return [index + 1 for index, value in enumerate(scores) if value == max(scores)]
    
    def other_solution_one(self, answers):
        student_answers = [
            [1, 2, 3, 4, 5],
            [2, 1, 2, 3, 2, 4, 2, 5],
            [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
        ]
        
        count = [0, 0, 0]
        
        for i in range(len(student_answers)):
            for j in range(len(answers)):
                if student_answers[i][j % len(student_answers[i])] == answers[j]:
                    count[i] += 1
        
        answer = []
        
        for i in range(len(student_answers)):
            if count[i] == max(count):
                answer.append(i + 1)
        
        return answer
    
    def other_solution_two(self, answers: List[int]) -> List[int]:
        pattern1 = [1, 2, 3, 4, 5]
        pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
        pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
        scores   = [0, 0, 0]
        result   = []
        
        for index, answer in enumerate(answers):
            if answer == pattern1[index % len(pattern1)]:
                scores[0] += 1
            
            if answer == pattern2[index % len(pattern2)]:
                scores[1] += 1
            
            if answer == pattern3[index % len(pattern3)]:
                scores[2] += 1
        
        for index, score in enumerate(scores):
            if score == max(scores):
                result.append(index + 1)
        
        return result


class TestSolution(unittest.TestCase):
    
    def setUp(self) -> None:
        self.solution = Solution()
        
        self.case_1 = [1, 2, 3, 4, 5]
        self.case_2 = [1, 3, 2, 4, 2]
        
        self.result_list = [
            [1],
            [1, 2, 3]
        ]
    
    @CommonUtils.logging_time
    def test_my_solution(self):
        result_list = [
            self.solution.my_solution(self.case_1),
            self.solution.my_solution(self.case_2)
        ]
        
        self.assertEqual(
            self.result_list,
            result_list
        )

    @CommonUtils.logging_time
    def test_best_solution(self):
        result_list = [
            self.solution.best_solution_i_think(self.case_1),
            self.solution.best_solution_i_think(self.case_2)
        ]
        
        self.assertEqual(
            self.result_list,
            result_list
        )

    @CommonUtils.logging_time
    def test_other_solution_one(self):
        result_list = [
            self.solution.other_solution_one(self.case_1),
            self.solution.other_solution_one(self.case_2)
        ]
    
        self.assertEqual(
            self.result_list,
            result_list
        )

    @CommonUtils.logging_time
    def test_other_solution_two(self):
        result_list = [
            self.solution.other_solution_two(self.case_1),
            self.solution.other_solution_two(self.case_2)
        ]

        self.assertEqual(
            self.result_list,
            result_list
        )


if __name__ == '__main__':
    unittest.main()

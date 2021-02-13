from typing import List


class Solution:
    """ 최대공약수와 최소공배수
    두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution 을 완성해 보세요.
    배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다.
    예를 들어 두 수 3, 12의 최대공약수는 3,
    최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.
    
    -최대공약수 : 두 수가 나눠지는 최대 값
    -최소공배수 : 두 수로 나눌 수 있는 최소 값
    
    제한 사항
        두 수는 1이상 1000000이하의 자연수입니다.
    
    입출력 예
        n   m   return
        3   12  [3, 12]
        2   5   [1, 10]
    """
    
    def my_solution(self, n: int, m: int) -> List[int]:
        """ 유클리드 호제법
        참조 링크 : https://m.blog.naver.com/PostView.nhn?blogId=writer0713&logNo=221133124302&proxyReferer=https:%2F%2Fwww.google.com%2F
        """
        
        temp_n = n
        temp_m = m
        gcd = 0
        
        while m > 0:
            gcd = m
            m = n % m
            n = gcd
        
        smn = int((temp_n * temp_m) / gcd)
        
        return [gcd, smn]
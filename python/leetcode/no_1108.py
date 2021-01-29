""" 1108. Defanging an IP Address

Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP address replaces every period "." with "[.]".

- 주어진 올바른 IP4 주소가 있다면, 제거된 버전의 IP 주소를 리턴하라.
- 제거된 버전의 IP 주소는 모든 . 를 [.] 로 교체한다.

Example 1:
    Input: address = "1.1.1.1"
    Output: "1[.]1[.]1[.]1"
    
Example 2:
    Input: address = "255.100.50.0"
    Output: "255[.]100[.]50[.]0"

Constraints:
    The given address is a valid IPv4 address.
"""
from python.utils import CommonUtils
import unittest


class Solution:
    
    @CommonUtils.logging_time
    def defangeIPAddress_by_replace(self, address: str) -> str:
        return address.replace('.', '[.]')
    
    @CommonUtils.logging_time
    def defangeIPAddress_by_join(self, address: str) -> str:
        return '[.]'.join(address.split('.'))
    
    @CommonUtils.logging_time
    def defangeIPAddress_by_re(self, address: str) -> str:
        import re
        return re.sub('\.', '[.]', address)
    
    @CommonUtils.logging_time
    def defangeIPAddress_by_for(self, address: str) -> str:
        return ''.join('[.]' if c == '.' else c for c in address)


class TestSolution(unittest.TestCase):
    
    def test_one_defangeIPAddress_by_replace(self):
        s = Solution()
        case_one = '1.1.1.1'
        result = s.defangeIPAddress_by_replace(case_one)
        self.assertEqual('1[.]1[.]1[.]1', result)
    
    def test_two_defangeIPAddress_by_replace_test_one(self):
        s = Solution()
        case_one = '255.100.50.0'
        result = s.defangeIPAddress_by_replace(case_one)
        self.assertEqual('255[.]100[.]50[.]0', result)
        

if __name__ == '__main__':
    unittest.main()
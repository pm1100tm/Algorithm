""" 1108. Defanging an IP Address

Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP address replaces every period "." with "[.]".

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


if __name__ == '__main__':
    solution = Solution()
    address_ex1 = "1.1.1.1"
    address_ex2 = "255.100.50.0"
    
    r1 = solution.defangeIPAddress_by_replace(address_ex1)
    r2 = solution.defangeIPAddress_by_join(address_ex1)
    r3 = solution.defangeIPAddress_by_re(address_ex1)
    r4 = solution.defangeIPAddress_by_for(address_ex1)
"""
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Note:
The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.
Example 1:
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
Example 2:
Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
"""

# the origin i = 1 which is 001 in binary code, and suppose num = 5
# then i << 1 on every loop,it will be like 0010,0100,1000,which is 2,4,8,then i -1 = 7, which is 0111 in binary,
# and the ^ calculation means get opposite,when 111^101,you will get 010,which is 2

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        if num == 0:
            return 1
        else:
            i = 1
            while i <= num:
                i = i << 1
            
            return num^(i-1)

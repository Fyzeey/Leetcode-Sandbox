"""
Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?

"""

# 这题不用loop/recursion的话要么用math.log要么就找greatest integer power of 3
# maximum int is 2**31 - 1 = 1162261467, Next val 3* 1162261467 is a long int
# 以下方法用了while loop

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:  
            return False
        
        while n % 3 == 0:
            n = n/3
        
        return n == 1
            

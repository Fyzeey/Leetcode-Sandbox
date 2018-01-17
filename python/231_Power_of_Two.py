"""
Given an integer, write a function to determine if it is a power of two.

"""

# 常用方法while loop, 速度慢
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        
        else:
            while n % 2 == 0:
                n = n / 2
            return n == 1
            
# 更legit的方法, 关键在于每个power of 2的int的binary representation 都只有一个bit是1，
# n & n - 1 removes the left most bit of n. 
# If an integer is power of 2, there is a single bit in the binary representation of n. 
# e.g. 16 = b10000, 16 - 1 = b01111, and 16 & 16 - 1 = b10000 & b01111 = 0, also 16 > 0
# based on these facts there is only one bit in b10000, so 16 is power of 2.

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and not (n & n-1)

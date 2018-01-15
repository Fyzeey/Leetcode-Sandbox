"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, 
replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
"""

# My own solution using recursive
# Passed with customized test case with input 13, but failed in submission(input 13)
class Solution(object):
    if_cycle = []

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        num_string = str(n)
        temp_sum = []
        for number in num_string:
            temp_sum.append(int(number) ** 2)

        if sum(temp_sum) == 1:
            return True
        elif sum(temp_sum) in self.if_cycle:
            return False
        else:
            self.if_cycle.append(sum(temp_sum))
            return self.isHappy(sum(temp_sum))
    
    
 # While loop approach
 class Solution(object):

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if_cycle = set()
        while n != 1:
            n = sum(int(i)**2 for i in str(n))
            if n in if_cycle:
                return False
            
            if_cycle.add(n)
        
        return True

"""
Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Example 1:
Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
Note:
n is a positive integer, which is in the range of [1, 10000].
All the integers in the array will be in the range of [-10000, 10000].

"""

# My solution is to sort the list first, and then return the sum of all values with even index
# This approach is slow, only beats 30.83% python submission
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # list.sort() mutate original list, if you want to return a new sorted list, use sorted() function instead
        nums.sort()
        return sum(nums[::2])
    
# For optimal solution, visit https://leetcode.com/problems/array-partition-i/discuss/102201

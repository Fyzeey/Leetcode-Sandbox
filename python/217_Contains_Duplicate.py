"""
Given an array of integers, find if the array contains any duplicates. 
Your function should return true if any value appears at least twice in the array, 
and it should return false if every element is distinct.
"""

# Easy appraoch but not efficient, use set to remove duplicate elements. 46ms
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_set = set(nums)
        if len(nums_set) == len(nums):
            return False
        else:
            return True
            
# Sort array first and traverse through it to check duplicate elements
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or len(nums) == 1:
            return False
        else:
            nums.sort()

            for num in range(len(nums)-1):
                if nums[num] == nums[num + 1]:
                    return True
            return False
        

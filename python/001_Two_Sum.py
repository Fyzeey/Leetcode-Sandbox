"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

# 这题用dictionary来存value和index，key和key.value相加等于target
# 以[2,7,11,15], target = 9 为例
# mydic = {
#   "7": 0
# }
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return False
        mydict = {}
        for i in range(0, len(nums)):
            # True, if a key num[i] exists in the dictionary d
            if nums[i] in mydict:
                return [mydict[nums[i]], i]
            else:
                mydict[target-nums[i]] = i

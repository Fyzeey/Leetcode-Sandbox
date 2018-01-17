"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""

# 这题不许extra space，不能counting sort
# 以下是自己写的原本的code， runtime 不是 O(n)
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res[]
        for x in xrange(1, len(nums)+1):
          if x in nums:
            pass
          else:
            res.append(x)
        
        return res
     
# 以下是用abs并且accepted的方法， 根据题目，假如没有missing number， 那么nums.sort()的num[index] = index + 1
# 每个数只能出现一次，任何duplicate都会导致missing number
# For each number i in nums,we mark the number that i points as negative. Then we filter the list, get all the indexes
# who points to a positive number. Since those indexes are not visited. 

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for x in xrange(len(nums)):
            # 这里abs不能少，否则重复rewrite的时候index会变成负数
            index = abs(nums[x])-1
            nums[index] = -abs(nums[index])
                               
        return [x+1 for x in range(len(nums)) if nums[x] > 0]
        

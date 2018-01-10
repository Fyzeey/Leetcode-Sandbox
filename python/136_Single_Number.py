"""
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        return sum(list(set(nums)))*2 - sum(nums)
    
 """
 一开始一直在想排序，用counting sort，可是不知道array element的数值范围
 解法1：element value range is in O(n)：
 
 class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = {}
        result = -1;
        for i in nums:
            if i in ret:
                ret[i]=0;
            else:
                ret[i]=1;

        for v in ret.keys():
            if(ret[v]==1): 
                result = v

        return result;
    
 解法2：
 解题的关键使用set()来remove duplicate elements, dedup后order会被打乱，因为set是unordered。
 下一步可以：
     1 以dedup的新list为reference，拿nums里每个element和reference比，缺点是runtime不是linear
     2 用求和（见code），这是一种讨巧的解法。
     
 Python里list,set,dictionary,turple的区别请见
 https://en.wikiversity.org/wiki/Python_Programming/Tuples_and_Sets
 
 Lists and tuples allow duplication. Dictionary and set items are unique.
 Sets may be used to remove duplication found in other data structures.
 
 
 """

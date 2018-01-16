"""
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""

# Anagram其实就是打乱字母顺序，每个字母出现的次数都要一样
# 直接把string转成list，sort后看他们是否相等
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        temp_s = list(s)
        temp_t = list(t)
        
        temp_s.sort()
        temp_t.sort()
        return temp_s == temp_t

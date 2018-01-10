"""
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
   
"""

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

"""
Extended slice syntax. 
It works by doing [begin:end:step] - by leaving begin and end off and specifying a step of -1, it reverses a string.
"""

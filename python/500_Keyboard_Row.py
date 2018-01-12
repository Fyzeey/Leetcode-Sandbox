"""
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.


American keyboard


Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet

"""

# Key idea is to use the bitwise operator & for set, and find intersection of two sets.
# Need to convert every word string into set
# Need to handle capital letters
# For more bitwise operation on set, visit https://docs.python.org/2/library/sets.html, Section 8.7.1

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row_one = set("qwertyuiop")
        row_two = set("asdfghjkl")
        row_three = set("zxcvbnm")
        
        result = []
        for word in words:
            word_set = set(word.lower())
            if row_one & word_set == word_set:
                result.append(word)
            if row_two & word_set == word_set:
                result.append(word)
            if row_three & word_set == word_set:
                result.append(word)   
        return result

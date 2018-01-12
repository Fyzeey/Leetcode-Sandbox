"""
Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.

Example 1:
Input: "UD"
Output: true
Example 2:
Input: "LL"
Output: false

"""

# My solution, didn't use count() function, which waste space and slow.
# My first submission is wrong becasue I only assign numerical value to each move, but didn't check whether the LR or UD are equal.
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        
        horizontal = []
        vertical = []
        for move in moves:
            if move == "U":
                vertical.append(1)
            elif move == "D":
                vertical.append(-1)
            elif move == "L":
                horizontal.append(1)
            elif move == "R":
                horizontal.append(-1)
            else:
                return None
        
        if sum(horizontal) == 0 and sum(vertical) == 0:
            return True
        else:
            return False
            
# Here is legit python one-line solution using count()function

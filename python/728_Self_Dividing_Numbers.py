"""
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Example 1:
Input: 
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
Note:

The boundaries of each input argument are 1 <= left <= right <= 10000.

"""

#The idea here is to convert each number into string therefore we can access each bit of that number
def is_selfDividing(num):
    # Convert each number in the list into string
    num_string = str(num)
    # Initialize counter to count successful division
    counter = 0
    for item in num_string:
        # Check if there is 0 in the number
        if item == "0":
            return False
        # The original number gets divided by each bit
        if num % int(item) == 0:
            counter += 1
    # Check if successful division equals the length of string (number of bits of original number)
    if counter == len(num_string):
        return True
    else:
        return False
    
    

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        for number in range(left, right+1):
            if is_selfDividing(number):
                result.append(number)
        return result

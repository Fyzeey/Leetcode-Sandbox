"""

Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
"""

# Bad solution too slow
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        result = []
        for number in range (n):
            result.append(str(number + 1))
            if int(result[number]) % 3 == 0 and int(result[number]) % 5 == 0:
                result[number] = "FizzBuzz"
            elif int(result[number]) % 3 == 0:
                result[number] = "Fizz"
            elif int(result[number]) % 5 == 0:
                result[number] = "Buzz"
            
        return result


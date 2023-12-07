class Solution(object):
    def largestOddNumber(self, num):
        # Given a number represented as a str
        # Return the largest odd number as a str, if no odd number exist return ""
        
        # Iterate the given number 
        for n in range(len(num)):
            # If given number is odd return it
            if int(num) % 2 != 0:
                return str(num)
            # If the number is even remove 1 digit
            else:
                num = num[:-1]
                print(num)
        # If no odd number is found return empty string
        return ""

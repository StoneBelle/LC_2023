class Solution(object):
    def addDigits(self, num):
        # Check if num is 0
        if num == 0:
            return 0
        # Check if num is divisible by 9
        elif (num % 9) == 0:
            return 9
        # If num is not 0 or divisible by 9 
        else:
            return num % 9 

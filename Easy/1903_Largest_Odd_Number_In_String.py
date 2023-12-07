class Solution(object):
    def largestOddNumber(self, num):
        # Variable to check if given number contains all even numbers
        index = -1

        # Iterate through each digit in given number
        for n in range(len(num)):
           
            # If an odd numberis found, replace the index with the odd number's index
            if int(num[n]) % 2 != 0:
                index = n
        
        # If all numbers in given number were even, index will still be -1, hence return empty string
        if index == -1:
            return ""
        
        # If odd number was found, slice given number from start, until the last odd number index +1 (due to slicing)
        # Return the sliced number as a string
        else:
            return(str(num[0:index+1]))

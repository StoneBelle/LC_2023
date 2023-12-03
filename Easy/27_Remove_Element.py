class Solution(object):
    def removeElement(self, nums, val):

        # Given a list & an integer 
        # Check if val exists in nums
        # If so, remove all occurences of integer val from nums array
        # Return the length of the the updated array

        while val in nums:
                nums.remove(val)
        
        return len(nums)

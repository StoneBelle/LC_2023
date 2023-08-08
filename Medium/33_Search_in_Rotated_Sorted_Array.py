class Solution(object):
    def search(self, nums, target):
        # Given a list nums - containing groups of distinct ascending values
        # Values can rotate (re-ascend) at an unknown pivot index (i.e. k)
        # Also given target - a value that is estimated to be where k is

        # If target is found, and values after target ascend return it 
        # Else return -1

        # Check if target is in nums
        if target not in nums:
            return -1
        else:
            return nums.index(target)
            


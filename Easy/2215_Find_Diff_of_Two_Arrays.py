class Solution(object):
    def findDifference(self, nums1, nums2):
  
        # Find missing ints for each array
        miss1 = {num for num in nums1 if num not in nums2}
        miss2 = {num for num in nums2 if num not in nums1}
        return [list(miss1), list(miss2)]


class Solution(object):
    def search(self, nums, target):
        # Determine if target is in nums
        # Must decrease overall operation steps

        # O(n) Time Complexity
        if target in nums:
            return True

        # 0(logn)

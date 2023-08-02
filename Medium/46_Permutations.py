from itertools import permutations

class Solution(object):
    def permute(self, nums):
        # Find all possible arrangements of nums
        return permutations(nums)

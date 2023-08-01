from itertools import combinations

class Solution(object):
    def combine(self, n, k):
    
        # Given n & k values
        # Create all possible combinations from 1 - n
        # Combinations must be the length of k 

        nums = [x for x in range(1, n + 1)]
        comb = combinations(nums, k)
        return comb

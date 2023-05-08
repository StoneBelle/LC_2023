from functools import reduce
from operator import mul

class Solution(object):
    def arraySign(self, nums):
        # Determine the product of given list
        p = reduce(mul, nums)

        # Based on product, return 1, -1, or 0
        if p == 0:
            return 0
        elif p > 0:
            return 1
        else:
            return -1

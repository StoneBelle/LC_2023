class Solution(object):
    def singleNumber(self, nums):
        # Count instances of each element
        num_count = Counter(nums)

        # Return the element with an instance of 1
        for key, value in num_count.items():
            if value == 1:
                return key

class Solution(object):
    def singleNonDuplicate(self, nums):
        
        # Create dict of for instances of each item in list
        count = Counter(nums)

        # Find element with value of 1
        count_vals = count.values()
        position = count_vals.index(1)

        # Return key of item found
        count_keys = count.keys()
        return count_keys[position]

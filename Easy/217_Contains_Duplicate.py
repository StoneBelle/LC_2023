class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # Count item instances
        n_instances = Counter(nums)
        # Return T if a item appears 2+ times
        vals = n_instances.values()
        for v in vals:
            if v >= 2:
                return True
       

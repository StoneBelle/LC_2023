class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Iterate through len(nums1)(i.e. m + n)
        for i in range(m + n):
            # Keep m items 
            if i < m:
                pass
            # Once m items passed, replace n items in nums1
            else: nums1[i] = nums2[i-m]
        nums1.sort()

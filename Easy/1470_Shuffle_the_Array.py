class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # Split nums into 2n parts
        n1 = nums[:n]
        n2 = nums[n:]

        # Add 2n items to empty list for range n
        a = []
        for z in range(n):
            a.append(n1[z])
            a.append(n2[z])
        return a        

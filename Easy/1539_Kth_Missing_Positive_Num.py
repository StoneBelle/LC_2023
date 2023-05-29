class Solution(object):
    def findKthPositive(self, arr, k):
        # Find which ints are missing from array & store in list      
        missing = [m for m in range(1, arr[-1] + 1 + k) if m not in arr]
        
        # Return kth item from missing list
        print(missing)
        return missing[k-1]

class Solution(object):
    def removeDuplicates(self, nums):
        # Given a list of ints, in non-decreasing order
        # Remove duplicates, keeping only 1 of each element 
        # Be sure maintain the reletive order of the elements
        # Return k - the number of unique elements in nums

        # Determine frequency of each element 
        nums_count = Counter()                          
        nums_count = Counter(nums) 
        
        # Find the elements that have duplicates
        duplicates = [n for n in nums_count if nums_count[n] >= 2]
       
       # Remove the duplicates from original array
        x = nums_count.items()
        for a, b in x:
            if a in duplicates:
                for c in range(b - 1):
                    nums.remove(a)
            
        # Remove the duplicates from given array
        return len(nums)
       

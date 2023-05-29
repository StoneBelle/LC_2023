from itertools import permutations

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool: 
        # Find all permutations of s1
        x = [''.join(p) for p in permutations(s1)]

        # Check if any s1 permutation is in s2
        for y in x:
            if y in s2:
                return True
        return False
        

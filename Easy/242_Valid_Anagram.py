class Solution(object):
    def isAnagram(self, s, t):
    
        # Convert s & t into sorted lists
        s_list = [ch for ch in s]
        t_list = [ch for ch in t]

        # Check if anagram can be formed
        return sorted(s_list) == sorted(t_list)

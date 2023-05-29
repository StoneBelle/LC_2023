class Solution(object):
    def strStr(self, haystack, needle):
        # Create variables to count, form & store potential needle
        find_n = needle[0]

        # Check if substring is in string
        if needle in haystack:
            # Iterate through len(haystack) to find start of needle
            for i in range(len(haystack) - len(needle) + 1): 
                # If start found, slice uhaystack until len(needle) & return i if match found
                if haystack[i] == find_n and haystack[i:i + len(needle)] == needle:
                    return i 
        else:
            return -1

        

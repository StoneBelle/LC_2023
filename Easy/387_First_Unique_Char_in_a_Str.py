class Solution(object):
    def firstUniqChar(self, s):
        # Count instance of each char 
        s_dict = Counter(s)
     
        # Iterate through s to check for 1st instance == 1
        y = -1
        for x in s:
            y += 1
            if s_dict[x] == 1:
                return y
        return -1
                

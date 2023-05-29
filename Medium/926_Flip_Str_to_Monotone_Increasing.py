class Solution:
    def minFlipsMonoIncr(self, s):
        num_0, num_1 = 0, 0
        for ch in s:
            if ch == '0':
                num_0 += 1
            else:
                num_1 += 1
           
            num_0 = min(num_0, num_1)
        return num_0

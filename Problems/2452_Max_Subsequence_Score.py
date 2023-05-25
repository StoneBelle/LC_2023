from itertools import combinations
class Solution(object):
    def maxScore(self, nums1, nums2, k):
 
        # Enumerate nums1 to track indices
        indices = enumerate(nums1)
        
        # Find all possible combinations
        comb = combinations(indices, k)
        score = 0
        s = 0
        x = []

        # Calculate subseq. score
        for indice in list(comb):
            for i in indice:
                s += i[1]
                x.append(i[0])
                min_nums2 = [nums2[y]for y in x]
                if score < s * min(min_nums2):
                    score = s * min(min_nums2)
            s = 0
            x = []

        return score

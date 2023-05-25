from itertools import combinations
class Solution(object):
    def maxScore(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """

        # Find all possible subsequence
        indices = enumerate(nums1)
        comb = combinations(indices, k)
        score = []

        # Determine index of subsequence
        for indice in list(comb):
            # sum of nums1 subseq.
            s = [i[1] for i in indice]
            # index of nums1 subseq.
            x = [i[0] for i in indice]
            
            # selected nums2 subseq.
            min_nums2 = [nums2[y]for y in x]
            
            # determine subseq. score
            score.append(sum(s) * min(min_nums2))
        return max(score)

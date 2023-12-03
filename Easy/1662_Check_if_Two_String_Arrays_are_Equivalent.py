class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        # Concatenate the elements in each list 
        w1 = "".join(word1)
        w2 = "".join(word2)

        # Check if concatenated words match
        if w1 == w2:
            return True

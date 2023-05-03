class Solution(object):
    def detectCapitalUse(self, word):
        # Ensure given input is within problem constraints
        if 1 <= len(word) <= 100 and word.isalpha():
            # Check word for proper use of capitalization. Return T/F
            if word.isupper() or word.islower() or word.istitle():
                return True
            else:
                return False

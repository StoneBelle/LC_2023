class Solution(object):
    def numberOfMatches(self, n):
       
        # Variable to track number of matches
        m = 0
        
        # Checks if number of teams is even or odd, then applies appropriate rules
        while n > 1:
            if n % 2 == 0:
                m += n / 2
                n = n / 2

            else:
                m += (n - 1) / 2 
                n = (n - 1) / 2 + 1

        return m
        
       

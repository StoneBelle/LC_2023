import numpy as np
class Solution(object):
    def diagonalSum(self, mat):
        # Creates numpy matrix
        m = np.matrix(mat)
        
        # Get primary & secondary diagonals
        pd = np.diagonal(m)
        sd = np.diag(np.fliplr(m))   
        
        # Check if diagonals len is odd (i.e. intersect)
        if len(pd) % 2 != 0:
            middle_index = len(pd) // 2 
            # Removes intersection from secondary diagonal
            new_sd = np. delete(sd, middle_index)
            return sum(pd) + sum(new_sd)
        # If diagonals is even (i.e no intersection)
        else:
            return sum(pd) + sum(sd)

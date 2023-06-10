class Solution(object):
    def countNegatives(self, grid):
        
        answer = 0
        for g in grid:
            for num in g:
                if num < 0:
                    answer += 1

        return answer

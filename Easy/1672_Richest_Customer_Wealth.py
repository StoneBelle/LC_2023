class Solution(object):
    def maximumWealth(self, accounts):
      
        wealth_sum = [sum(acc)for acc in accounts]
        return max(wealth_sum)

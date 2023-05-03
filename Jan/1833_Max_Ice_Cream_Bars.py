class Solution(object):
    def maxIceCream(self, costs, coins):
         # Check if ALL bars can be purchased
        total_sell_price = sum(costs)
        if total_sell_price <= coins:
            return len(costs)

        # Check if NO bars can be purchased
        lowest_unit_price = min(costs)
        if lowest_unit_price > coins:
            return 0
      
        # Check which bars can be purchased
        cart = 0
        within_budget = [bar for bar in costs if bar <= coins]
        within_budget.sort()
        for c in within_budget:
            if coins - c >= 0:
                coins -= c
                cart += 1
        return cart

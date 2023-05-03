class Solution(object):
    def maxIceCream(self, costs, coins):
        # Remove bars above budget, and sort remaining bars
        # Incrementally subtract cost from coins until no more bars can be bought
        cart = 0
        within_budget = [bar for bar in costs if bar <= coins]
        within_budget.sort()
        for c in within_budget:
            if coins - c >= 0:
                coins -= c
                cart += 1
        return cart

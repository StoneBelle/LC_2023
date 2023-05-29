class Solution:
    def totalFruit(self, fruits: List[int]) -> int: 

        # numbers in list represent type of fruit
        # can only pick 2 types of fruit
        # return MAX amount trees you can pick from
        basket= {}
        start= 0
        for fruit in fruits:
            basket[fruit]= basket.get(fruit, 0) + 1

            if len(basket)> 2:
                basket[fruits[start]]-= 1
                if basket[fruits[start]]== 0:
                    del basket[fruits[start]]
                start+= 1
        
        return len(fruits)- start

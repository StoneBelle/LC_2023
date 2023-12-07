from itertools import combinations

class Solution(object):
    def largestOddNumber(self, num):
        # Given a number represented as a str
        # Return the largest odd number as a str, if no odd number exist return ""

        if int(num) % 2 != 0:
            return str(num)
        else:
            # Find all posible odd number combinations, and store in list
            all_comb = [num[x:y] for x, y in combinations(range(len(num) + 1), r = 2)]            

            odd_comb = [x for x in all_comb if int(x) % 2 != 0]
            print(odd_comb)
            # Return the largest odd number as a str, if no odd number exist return ""
            if len(odd_comb) == 0:
                return ""
            else:
                # Converts elements in odd_comb from unicode to int
                answr = max(map(int, odd_comb))
                return str(answr)

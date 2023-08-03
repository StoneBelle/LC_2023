from itertools import product
class Solution(object):
    def letterCombinations(self, digits):
        # Letter values for digits 2-9
        my_dict = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        my_letters = []

        # Check if digits is empty
        if len(digits) == 0:
            return []
        else:
            # Retrieve letters from given digit(s) & store in list
            for x in digits:
                my_letters.append(my_dict.get(x))

            # Determines all possible letter combinations
            answr = ["".join(x) for x in product(*my_letters)]
            return answr

     
        

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        # Join all items in num 
        str_num = map(str, num)
        n = "".join(str_num)
        
        # Add joined num and k together 
        n_sum = int(n) + k    

        # Place individual ints of added number into a list
        answr = [int(x) for x in str(n_sum)]
        return answr

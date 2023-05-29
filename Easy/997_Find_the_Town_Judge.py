class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Given a list of list of ints
        # trust[i] = [ai, bi]
        # Find the town judge
        # Conditons are:
        # ai = people
        # bi = judge
        # if bi is not the same for all ai, judge cannot be identified

        # Store potential judge in variable        
        j = trust[0][1]
        # Iterate through each person
        for t in trust:
            # If bi differs from j, return -1
            if t[1] != j:
                return -1  
        return j

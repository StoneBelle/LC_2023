class Solution(object):
    def minimumRounds(self, tasks):
        # identify all different types & frequency for each type
        # t_types = set(tasks)
        # t_freq = {t: tasks.count(t) for t in t_types}
        # running lines 4-5 gets the same answer but exceeds Time Limit. 
       
        t_freq = Counter(tasks) # replaces lines 4-5 to stay witin Time Limit

        rounds = 0
        for f in t_freq.values():
            while f != 0:
                if f == 1:
                    return -1
                elif f % 3 == 0:
                    f -= 3
                    rounds += 1
                else:
                    f -= 2
                    rounds += 1
        return rounds


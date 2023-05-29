class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        s_total = []
        for x in range(len(mat)):
            s_count = Counter(mat[x])
            s = s_count[1]
            s_total.append((s, x))
        s_total.sort()
        weakest_rows = [s_total[w][1] for w in range(k)]

        return weakest_rows

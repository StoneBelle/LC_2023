class Solution(object):
    def minDeletionSize(self, strs):
        # Ensure given input meets problem constraints
        if 1 <= len(strs) <= 100 and 1 <= len(strs[0]) <= 1000:
            for s in strs:
                if not s.isalpha():
                    return "Invalid Input"

        # Assemble columns based on index of each char in each row
        rows = [s.lower() for s in strs]
        cols = []
        col_item = ""
        row_counter = 0
        for ch in range(len(rows[0])):
            for row in rows:
                col_item = col_item + row[ch]
                row_counter += 1
                if row_counter == len(rows):
                    cols.append(col_item)
                    row_counter = 0
                    col_item = ""

        # Check and return an int for total number of unsorted columns
        not_sorted = 0
        for col in cols:
            check_col = list(col)
            sorted_col = sorted(check_col)
            if check_col != sorted_col:
                not_sorted += 1

        return not_sorted

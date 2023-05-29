class Solution(object):
    def addDigits(self, num):
        def separate_digits(n):
            """Separates digits in given num and return the sum of separated digits."""
            nums = map(int, str(n))
            n_sum = sum(nums)
            return n_sum

        # Check if num is 0
        if num == 0:
            return 0

        # Check if num is single digit
        else:
            answr = separate_digits(num)
            while answr > 9:
                a = separate_digits(answr)
                answr = a
            return answr

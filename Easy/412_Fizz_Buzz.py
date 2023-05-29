class Solution(object):
    def fizzBuzz(self, n):
        x_list = []
        num = 0
        for x in range(n):
            num += 1
            if num % 3 == 0 and num % 5 == 0:
                x_list.append("FizzBuzz")
            elif num % 5 == 0:
                x_list.append("Buzz")
            elif num % 3 == 0:
                x_list.append("Fizz")
            else:
                x_list.append(str(num))
        return x_list

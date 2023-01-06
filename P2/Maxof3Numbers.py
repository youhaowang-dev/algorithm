# https://www.lintcode.com/problem/283/description
# Given 3 integers, return the max of them.


class Maxof3Numbers:
    def max_of_three_numbers(self, num1: int, num2: int, num3: int):
        return self.get_max(num1, self.get_max(num2, num3))

    def get_max(self, num1: int, num2: int):
        if num1 < num2:
            return num2
        else:
            return num1

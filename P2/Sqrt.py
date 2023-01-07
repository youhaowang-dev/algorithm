# tag: Math, Binary Search
# Amazon 6 Bloomberg 4 Apple 4 Microsoft 3 Facebook 2 Google 2 LinkedIn 11 Adobe 6 Uber 2
# source: https://leetcode.com/problems/sqrtx/description/

# Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
# The returned integer should be non-negative as well.
# You must not use any built-in exponent function or operator.
# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

# Example 1:
# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.

# Example 2:
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.


from math import ceil


class Sqrt:
    # binary search int
    def sqrtInt(self, number: int) -> int:
        if number <= 1:
            return number

        left = 1
        right = number
        while left + 1 < right:
            mid = (left + right) // 2
            #   number / mid # avoid mid * mid overflow
            current_number = mid * mid
            if current_number == number:
                return mid
            if current_number > number:
                right = mid
            if current_number < number:
                left = mid

        if left * left <= number:
            return left

        if right * right <= number:
            return right

        raise Exception("sqrt not found")

    # binary search float
    def sqrtDouble(self, number: float, precise: float) -> float:
        left = 0
        right = number
        while left + precise < right:
            mid = (left + right) / 2
            if number - mid * mid == precise:
                return mid
            if number > mid * mid:
                left = mid
            if number < mid * mid:
                right = mid
        if right * right < number and number - right * right <= precise:
            return right
        if left * left < number and number - left * left <= precise:
            return left

        return left

    def sqrtDoubleLinearSearch(self, number: int, precise: float) -> float:
        n = 0
        while ((n + 1) * (n + 1)) <= number:
            n += 1
        while (n + precise) * (n + precise) <= number:
            n += precise
        return n

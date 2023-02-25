# Math
# Amazon 11 Apple 9 Adobe 7 Bloomberg 5 Microsoft 3 tcs 3 Oracle 2 Google 2 Uber 2 Intel 2 Facebook 6 Yahoo 3 Infosys 3 Visa 2 IBM 2 American Express 6 eBay 4 Samsung 2 Accenture 2
# https://leetcode.com/problems/reverse-integer/
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:
# Input: x = 123
# Output: 321
# Example 2:
# Input: x = -123
# Output: -321
# Example 3:
# Input: x = 120
# Output: 21
class ReverseInteger:

    # time: O(log(number)) total digits bounded by log10(number)
    # space: O(1)
    # 2147483647
    INT_MAX = 2**31 - 1
    INT_MAX_LAST = 7
    # -2147483648
    INT_MIN = -(2**31)
    INT_MAX_LAST = 8

    # python negative division and modulo behave differently from C++/Java
    # so convert number to positive and record the sign
    def reverse(self, number: int) -> int:
        print(self.INT_MIN, self.INT_MIN // 10)
        sign = 1 if number >= 0 else -1
        number = number if number >= 0 else -number
        reversed_number = 0
        while number != 0:
            digit = number % 10
            number = number // 10
            if self.appendWillOverflow(reversed_number, digit):
                return 0

            reversed_number = reversed_number * 10 + digit

        return reversed_number * sign

    def appendWillOverflow(self, number: int, digit: int) -> bool:
        exceedMaxWithoutAppending = number > (self.INT_MAX // 10)
        exceedMaxWithAppending = (
            number == self.INT_MAX / 10 and digit > self.INT_MAX_LAST
        )
        exceedMinWithoutAppending = number < (self.INT_MIN // 10)
        exceedMinWithAppending = (
            number == self.INT_MIN / 10 and digit < self.INT_MIN_LAST
        )

        return (
            exceedMaxWithoutAppending
            or exceedMaxWithAppending
            or exceedMinWithoutAppending
            or exceedMinWithAppending
        )

# Math, String, Simulation
# Microsoft 5 Facebook 2 Amazon 2 Google 2 Houzz 2 Two Sigma 2 Bloomberg 3 Yahoo 2 TikTok 2 Apple 9 Adobe 4 Square 2 VMware 2 Tesla 2 Yandex 2 Twitter
# https://leetcode.com/problems/multiply-strings/

# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

# Example 1:
# Input: num1 = "2", num2 = "3"
# Output: "6"
# Example 2:
# Input: num1 = "123", num2 = "456"
# Output: "56088"

# O(m*n)
# 123 * 45
# 3 5 =>           1, 5
#        [0, 0, 0, 1, 5]
# 3 4 =>        1, 2
#        [0, 0, 1, 3, 5]
# 2 5 =>        1, 0
#        [0, 0, 2, 3, 5]
# 2 4 =>     0, 8
#        [0, 1, 0, 3, 5]
# 1 5 =>     0, 5
#        [0, 1, 5, 3, 5]
# 1 4 =>  0, 4
#        [0, 5, 5, 3, 5]
class MultiplyStrings:
    def multiply(self, num1: str, num2: str) -> str:
        if not num1 or not num2:
            return ""

        digits = [0] * (len(num1) + len(num2))
        for i in reversed(range(len(num1))):
            for j in reversed(range(len(num2))):
                right_digit_index = i + j + 1
                left_digit_index = i + j
                digits[right_digit_index] += int(num1[i]) * int(num2[j])
                # might be > 9
                digits[left_digit_index] += digits[right_digit_index] // 10
                digits[right_digit_index] %= 10

        first_non_zero = 0
        while first_non_zero < len(digits) and digits[first_non_zero] == 0:
            first_non_zero += 1
        digits = digits[first_non_zero:]

        if not digits:
            return "0"

        str_digits = list()
        for digit in digits:
            str_digits.append(str(digit))

        return "".join(str_digits)

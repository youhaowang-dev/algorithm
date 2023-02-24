# Math, String, Bit Manipulation, Simulation
# https://leetcode.com/problems/add-binary
# Given two binary strings a and b, return their sum as a binary string.

# Example 1:
# Input: a = "11", b = "1"
# Output: "100"
# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"
class AddBinary:
    def addBinary(self, num1: str, num2: str) -> str:
        if not num1:
            return num2
        if not num2:
            return num1

        num1_digits = list(num1)
        num2_digits = list(num2)
        carry = 0
        result = deque()
        while num1_digits or num2_digits or carry:
            total = 0
            total += carry
            if num1_digits:
                total += int(num1_digits.pop())
            if num2_digits:
                total += int(num2_digits.pop())
            result.appendleft(str(total % 2))  # total can be 0 1 2 3
            carry = total // 2

        return "".join(result)

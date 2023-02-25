# String
# Amazon 9 Microsoft 5 Bloomberg 5 Apple 4 Adobe 4 Facebook 25 Google 7 Goldman Sachs 5 Redfin 3 Uber 2 Qualcomm 2 LinkedIn 3 Splunk 3 Qualtrics 3 eBay 2 VMware 2 Cisco 2 Intel 2
# https://leetcode.com/problems/string-to-integer-atoi/description/
# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

# good question but bad test cases, not all the edge cases will be in an interview, so
# make sure to ask enough questions and ask for unhandled cases(likely throw)

# We need to handle the followings.
# whitespaces, sign, overflow, invalid input
class StringtoInteger:
    INT_MAX = 2**31 - 1
    INT_MIN = -(2**31)

    def myAtoi(self, inputString: str) -> int:
        if not inputString:
            return 0

        i = 0
        # whitespaces
        while i < len(inputString) and inputString[i] == " ":
            i += 1
        if i >= len(inputString):
            return 0

        # sign
        sign = 1
        if inputString[i] == "-" or inputString[i] == "+":
            if inputString[i] == "-":
                sign = -1
            i += 1  # still need to skip +

        # build integer and check overflow and bad input
        number = 0
        while i < len(inputString) and inputString[i] >= "0" and inputString[i] <= "9":
            digit = int(inputString[i])
            if number > self.INT_MAX // 10 or (
                number == self.INT_MAX // 10 and digit > self.INT_MAX % 10
            ):
                return self.INT_MAX if sign == 1 else self.INT_MIN
            number = 10 * number + digit
            i += 1

        return number * sign

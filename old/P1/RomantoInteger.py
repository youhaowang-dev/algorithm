# Hash Table, Math, String
# Amazon 31 Adobe 26 Apple 25 Google 21 Microsoft 14 Facebook 8 Bloomberg 6 Yahoo 4 Oracle 3 tcs 2 Uber 4 TikTok 4
# Intel 2 Qualtrics 2 Morgan Stanley 2 Yandex 2 Accenture 2 Qualcomm 5 LinkedIn 4 JPMorgan 3 HBO 3 VMware 2
# Goldman Sachs 2 Flipkart 2
# https://leetcode.com/problems/roman-to-integer/

# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

# Example 1:
# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

# parse the string, check 2 chars first, if 2 chars are invalid, check 1 char
# another strategy is to replace IV,... with IIII, then process the new string
class RomantoInteger:
    ROMAN_TO_NUM = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        # four or nine
        "IV": 4,
        "XL": 40,
        "CD": 400,
        "IX": 9,
        "XC": 90,
        "CM": 900,
    }

    def romanToInt(self, s: str) -> int:
        result = 0
        if not s:
            return result

        char_index = 0
        while char_index < len(s):
            # check two chars first
            if (
                char_index + 1 < len(s)
                and s[char_index] + s[char_index + 1] in self.ROMAN_TO_NUM
            ):
                result += self.ROMAN_TO_NUM[s[char_index] + s[char_index + 1]]
                char_index += 2
            else:
                result += self.ROMAN_TO_NUM[s[char_index]]
                char_index += 1

        return result

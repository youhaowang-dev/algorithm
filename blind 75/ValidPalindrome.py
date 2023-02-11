# Two Pointers, String
# https://leetcode.com/problems/valid-palindrome/
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and
# removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters
# include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

# two pointers, find valid left and right, compare and continue
class ValidPalindrome:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True

        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():  # find valid left
                left += 1
            while left < right and not s[right].isalnum():  # find valid right
                right -= 1
            if left < right and s[left].lower() != s[right].lower():  # compare
                return False
            # move pointers
            left += 1
            right -= 1

        return True

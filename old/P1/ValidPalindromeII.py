# Two Pointers, String, Greedy
# Facebook 30 Microsoft 2 Apple 2 2 7 TikTok 2 Amazon 2 Oracle 6 Walmart Global Tech 4 Bloomberg 3 Google 2 eBay Yahoo
# https://leetcode.com/problems/valid-palindrome-ii/description/

# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

# Example 1:
# Input: s = "aba"
# Output: true

# Example 2:
# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.

# Example 3:
# Input: s = "abc"
# Output: false

# continue is_palindrome validation if mismatch is found by ignoring left or right
class ValidPalindromeII:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                delete_left_is_palindrome = self.is_palindrome(s, left + 1, right)
                delete_right_is_palindrome = self.is_palindrome(s, left, right - 1)
                return delete_left_is_palindrome or delete_right_is_palindrome

            left += 1
            right -= 1

        return True

    def is_palindrome(self, s: str, left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True

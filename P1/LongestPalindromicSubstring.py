# String, Dynamic Programming
# Amazon 25 Cisco 10 Google 6 Bloomberg 6 Adobe 6 Microsoft 4 Uber 4 Goldman Sachs 4 Infosys 4 Facebook 3
# Apple 2 Oracle 2 Salesforce 2 MakeMyTrip 2 Yahoo 6 Visa 5 Walmart Global Tech 5 Expedia 2 Qualtrics 2 Qualcomm 2
# Zoho 2 Samsung 2 tcs 2 TikTok 2 ShareChat 2 Wayfair 12 eBay 6 ByteDance 6 PayTM 5 LinkedIn 3 Docusign 3 Intel 3
# Tesla 3 VMware 2 Yandex 2 Paypal 2 Grab 2 HBO 2 Softwire 2 Mercari 2 Wix
# https://leetcode.com/problems/longest-palindromic-substring/

# Given a string s, return the longest palindromic substring in s.

# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:
# Input: s = "cbbd"
# Output: "bb"


# brute force: O(2^n) try every substring

from typing import Tuple


# two pointers expand from middle
# time O(n^2) space 1
class LongestPalindromicSubstring:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return 0

        start = 0
        end = 0
        for i in range(len(s)):
            start1, end1 = self.get_range(s, i, i)
            start2, end2 = self.get_range(s, i, i + 1)
            if end1 - start1 > end - start:  # compare distance
                start, end = start1, end1
            if end2 - start2 > end - start:
                start, end = start2, end2

        return s[start:end + 1]

    def get_range(self, s: str, start: int, end: int) -> Tuple[int, int]:
        while start >= 0 and end < len(s):
            if s[start] == s[end]:
                start -= 1
                end += 1
            else:
                break
        start += 1  # different char, revert back one step
        end -= 1

        return start, end


# dp O(n^2)
class LongestPalindromicSubstring2:
    def longestPalindrome(self, input: str) -> str:
        length = len(input)
        is_palindrome = [[False for i in range(length)] for j in range(length)]
        for i in range(length):
            is_palindrome[i][i] = True
        longest_palindrome_start = 0
        longest_palindrome_len = 1

        for end in range(0, length):
            for start in range(end - 1, -1, -1):
                if input[start] == input[end]:
                    if end - start == 1 or is_palindrome[start + 1][end - 1]:
                        is_palindrome[start][end] = True
                        palindrome_len = end - start + 1
                        if longest_palindrome_len < palindrome_len:
                            longest_palindrome_start = start
                            longest_palindrome_len = palindrome_len
        return input[
            longest_palindrome_start: longest_palindrome_start + longest_palindrome_len
        ]

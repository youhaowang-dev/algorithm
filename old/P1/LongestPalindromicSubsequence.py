# https://leetcode.com/problems/longest-palindromic-subsequence
# Given a string s, find the longest palindromic subsequence's length in s.

# A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

# Example 1:
# Input: s = "bbbab"
# Output: 4
# Explanation: One possible longest palindromic subsequence is "bbbb".
# Example 2:
# Input: s = "cbbd"
# Output: 2
# Explanation: One possible longest palindromic subsequence is "bb".

class LongestPalindromicSubsequence:
    def longestPalindromeSubseq(self, s: str) -> int:
        if not s:
            return 0
        memo = dict()
        return self.get_max_length(s, 0, len(s) - 1, memo)

    def get_max_length(self, s, left, right, memo):
        if (left, right) in memo:
            return memo[(left, right)]
        if left == right:
            memo[(left, right)] = 1
            return 1
        if left > right:  # case like "aa"
            memo[(left, right)] = 0
            return 0
        if s[left] == s[right]:
            max_length = 2 + self.get_max_length(s, left + 1, right - 1, memo)
            memo[(left, right)] = max_length
            return max_length
        else:
            max_length = max(
                self.get_max_length(s, left + 1, right, memo),
                self.get_max_length(s, left, right - 1, memo)
            )
            memo[(left, right)] = max_length

            return max_length

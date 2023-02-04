# Hash Table, String, Greedy
# https://leetcode.com/problems/longest-palindrome/
# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome
# that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

# Example 1:
# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
# Example 2:
# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.

# palindrome = n pairs of same char + 0 or 1 unique char
# length = pair count * 2 + 1 if has odd count
# count char and count all the odd count, construct the palindrome
# time: O(n) space: O(n) for all unique characters
class LongestPalindrome:
    def longestPalindrome(self, s: str) -> int:
        if not s:
            return 0

        char_to_count = dict()
        for letter in s:
            char_to_count[letter] = 1 + char_to_count.get(letter, 0)

        pair_count = 0
        odd_count = 0
        for val in char_to_count.values():
            pair_count += val // 2
            odd_count += val % 2

        if odd_count > 0:
            return pair_count * 2 + 1

        return pair_count * 2

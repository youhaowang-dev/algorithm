# Hash Table, String, Sliding Window
# Amazon 12 Lyft 8 Apple 4 Airbnb 3 Facebook 2 Yandex 2 Oracle 2 LinkedIn 9 Microsoft 8 Adobe 8 Google 5
# Spotify 3 Uber 2 Snapchat 2 ByteDance 4 Bloomberg 3 Flipkart 3 Nagarro 3 VMware 2 Visa 2 TikTok 2 SAP 2 Qualtrics 2
# https://leetcode.com/problems/minimum-window-substring/
# Given two strings s and t of lengths m and n respectively, return the minimum window  substring
# of s such that every character in t (including duplicates) is included in the window.
# If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

# Example 1:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

# Example 2:
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.

# Example 3:
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.

# sliding window
# maintain a char_to_count dict and a need_count
# count > 0 means target char in substr, so need_count -= 1
# when need_count is 0, record the min window and try to move left while

# "abcde" find "bd", expect "bd"
# need_count:2      char_to_count: {'b': 1, 'd': 1}
# need_count:2      char_to_count: {'b': 1, 'd': 1, 'a': -1}
# need_count:1      char_to_count: {'b': 0, 'd': 1, 'a': -1}
# need_count:1      char_to_count: {'b': 0, 'd': 1, 'a': -1, 'c': -1}
# need_count:0      char_to_count: {'b': 0, 'd': 0, 'a': -1, 'c': -1}    => update
# need_count:1      char_to_count: {'b': 1, 'd': 0, 'a': 0, 'c': -1, 'e': -1}
class MinimumWindowSubstring:
    def minWindow(self, string: str, target: str) -> str:
        if not string or not target:
            return ""

        char_to_count = collections.Counter(target)

        left = 0
        right = 0
        min_window = ""
        need_count = len(target)
        while right < len(string):
            # make need_count == 0
            char_to_count[string[right]] -= 1
            if char_to_count[string[right]] >= 0:
                need_count -= 1
            # make need_count > 0
            while need_count == 0:
                window_len = right - left + 1
                if not min_window or window_len < len(min_window):
                    min_window = string[left: right + 1]

                char_to_count[string[left]] += 1
                if char_to_count[string[left]] > 0:
                    need_count += 1

                left += 1

            right += 1

        return min_window

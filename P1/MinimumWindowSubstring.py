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
# maintain a char_to_count dict and a required_count
# count > 0 means target char in substr, so required_count -= 1
# when required_count is 0, record the min window and try to move left while

# "abcde" find "bd", expect "bd"
# required_count:2      target_char_to_count: {'b': 1, 'd': 1}
# required_count:2      target_char_to_count: {'b': 1, 'd': 1, 'a': -1}
# required_count:1      target_char_to_count: {'b': 0, 'd': 1, 'a': -1}
# required_count:1      target_char_to_count: {'b': 0, 'd': 1, 'a': -1, 'c': -1}
# required_count:0      target_char_to_count: {'b': 0, 'd': 0, 'a': -1, 'c': -1}    => update
# required_count:1      target_char_to_count: {'b': 1, 'd': 0, 'a': 0, 'c': -1, 'e': -1}
class MinimumWindowSubstring:
    def minWindow(self, search_string: str, target: str) -> str:
        target_char_to_count = dict()
        for char in target:
            target_char_to_count[char] = 1 + target_char_to_count.get(char, 0)

        left = 0
        right = 0
        min_window = ""
        required_count = len(target)

        for right in range(len(search_string)):
            required_count = self.update_required_count(
                search_string, target_char_to_count, right, required_count
            )

            while required_count == 0:
                window_len = right - left + 1
                if not min_window or window_len < len(min_window):
                    min_window = search_string[left : right + 1]

                target_char_to_count[search_string[left]] += 1

                if target_char_to_count[search_string[left]] > 0:
                    required_count += 1

                left += 1

        return min_window

    def update_required_count(
        self, search_string, target_char_to_count, right, required_count
    ):
        right_char = search_string[right]
        right_char_count = target_char_to_count.get(right_char, 0)
        if right_char_count > 0:
            required_count -= 1

        target_char_to_count[right_char] = -1 + right_char_count

        return required_count

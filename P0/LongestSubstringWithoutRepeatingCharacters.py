# Hash Table, String, Sliding Window
# Amazon 32 Bloomberg 30 Adobe 14 Microsoft 12 Apple 11 Yandex 5 Google 4 Facebook 4 eBay 4 Uber 4 Yahoo 3
# Goldman Sachs 3 Spotify 3 Expedia 2 Visa 2 Nagarro 2 tcs 2 TikTok 2 Accenture 2 Walmart Global Tech 5 VMware 5
# Zoho 5 Paypal 4 Oracle 4 JPMorgan 4 Cisco 3 Intuit 3 Salesforce 3 Zillow 3 PayTM 3 Infosys 3 Alibaba 2 Twitch 2
# Samsung 2 Sumologic 2 Huawei 2 Capital One 2 Qualcomm 2 Docusign 2 American Express 2 IBM 2 Rubrik 2 Airtel 2
# Alation 4 SAP 4 ServiceNow 4 FactSet 3 Lyft 2 Morgan Stanley 2 Nvidia 2 Shopee 2 Yelp
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# two pointers, the window can increase when fast pointer val is not in current window
class LongestSubstringWithoutRepeatingCharacters:
    def lengthOfLongestSubstring(self, input_str: str) -> int:
        max_substr_length = 0

        substr_characters = set()
        left = 0
        right = 0
        while right < len(input_str):
            if input_str[right] in substr_characters:
                substr_characters.remove(input_str[left])
                left += 1
            else:
                substr_length = right - left + 1
                max_substr_length = max(max_substr_length, substr_length)
                substr_characters.add(input_str[right])
                right += 1

        return max_substr_length


# brute force: try all substrings and validate them
# time O(n^3)
class LongestSubstringWithoutRepeatingCharacters2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)

        res = 0
        for i in range(length):
            for j in range(i, length):
                if self.has_no_duplicate(i, j):
                    res = max(res, j - i + 1)
        return res

    def has_no_duplicate(self, s, start, end):
        chars = set()
        for i in range(start, end + 1):
            char = s[i]
            if char in chars:
                return False
            chars.add(char)

        return True

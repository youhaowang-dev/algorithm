# String, Trie
# Amazon 19 Apple 13 Google 10 Adobe 6 Microsoft 4 Uber 4 Facebook 3 Zoho 3 Yahoo 2 Expedia 2 Bloomberg 2 SAP 4
# Quora 3 Oracle 2 Visa 2 Walmart Global Tech 2 ByteDance 2 Snapchat 2 tcs 2 Accenture 2 Capgemini 2 Cisco 4 Intel 3
# eBay 2 VMware 2 IBM 2 Paypal 2 Nutanix 2 Epam Systems 2 Cognizant 2 persistent systems 2 Yelp
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

from ast import List

# find the shortest string and compare with
# The upper bound of the longest common prefix among the set of strings is the length of the shortest element
# in that set of strings. A common prefix that is longer than the shortest element in the list cannot exist.
# ["abcd","abc","ab"] => compare ab with others, a:a a:a a:a OK, b:b b:b b:b OK, end
class LongestCommonPrefix:
    def longestCommonPrefix(self, input_strings: List[str]) -> str:
        if not input_strings:
            return ""
        # shortest = min(input_strings, key=len)
        shortest = self.get_shortest(input_strings)
        for i, character in enumerate(shortest):
            for input_string in input_strings:
                if input_string[i] != character:
                    return shortest[:i]

        return shortest

    def get_shortest(self, input_strings: List[str]) -> str:
        shortest = input_strings[0]
        for str in input_strings:
            if len(shortest) > len(str):
                shortest = str

        return shortest

# Hash Table, String, Sorting
# Amazon 20 Bloomberg 19 Spotify 3 Google 2 Goldman Sachs 2 Apple 2 Yahoo 2 Microsoft 7 Facebook 6 Affirm 3 Yandex 2
# Qualcomm 2 Tesla 2 JPMorgan 5 Oracle 4 Cisco 4 Snapchat 3 Adobe 3 Walmart Global Tech 3 BlackRock 3
# American Express 3 Grab 2 IBM 2 Visa 2 Dell 2 Uber Yelp

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false

# brute force: sort
# dict to count freq, time O(n), space O(1) if only english character O(n) if not
class ValidAnagram:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_to_count = dict()
        for letter in s:
            char_to_count[letter] = 1 + char_to_count.get(letter, 0)

        for letter in t:
            char_to_count[letter] = -1 + char_to_count.get(letter, 0)
            if char_to_count[letter] == 0:
                del char_to_count[letter]

        # return not char_to_count
        return len(char_to_count) == 0

    def isAnagram2(self, s, t):  # bucket count
        dic1, dic2 = [0]*26, [0]*26
        for item in s:
            dic1[ord(item)-ord('a')] += 1
        for item in t:
            dic2[ord(item)-ord('a')] += 1
        return dic1 == dic2

    def isAnagram3(self, s, t):
        return sorted(s) == sorted(t)

# https://leetcode.com/problems/find-all-anagrams-in-a-string/
# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:
# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
class FindAllAnagramsinaString:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not s or not p or len(s) < len(p):
            return list()

        p_count = collections.Counter(p)
        window_count = collections.Counter(s[:len(p)])
        result = list()
        left = 0
        right = len(p) - 1
        while right < len(s):
            if window_count == p_count:
                result.append(left)

            window_count[s[left]] -= 1
            if window_count[s[left]] == 0:
                del window_count[s[left]]

            if right + 1 < len(s):
                window_count[s[right+1]] += 1
            left += 1
            right += 1

        return result

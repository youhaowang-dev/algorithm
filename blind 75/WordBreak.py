# Hash Table, String, Dynamic Programming, Trie, Memoization
# Amazon 19 Bloomberg 11 Facebook 7 Wish 5 Apple 4 Adobe 4 Google 2 Microsoft 2 TikTok 2 Qualtrics 4 Oracle 3 Walmart Global Tech 3
# Twitter 2 eBay 2 Yahoo 2 Salesforce 2 Cohesity 2 Uber 10 ByteDance 6 Snapchat 3 LinkedIn 2 Nvidia 2 Visa 2 Swiggy 2 Goldman Sachs 2 Pocket Gems Square Coupang
# https://leetcode.com/problems/word-break/

# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

# Example 1:
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:
# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.
# Example 3:
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false

# brute force dfs: if current substring in words, continue the search
# time n*2^n, for case like "aaa....",[a,aa,aaa....], all subsets will be generated and each subset costs n
# space n for max recursion depth

# memoized dfs
# time: O(n^3), O(n^2) substrings and creating each substring costs O(n)
# space: O(n^2) for all substrings
class WordBreak:
    def wordBreak(self, word: str, wordDict: List[str]) -> bool:
        if not word or not wordDict:
            return False

        word_has_break = dict()
        return self.has_break(word, set(wordDict), word_has_break)

    def has_break(self, word, words, word_has_break):
        if word in word_has_break:
            return word_has_break[word]
        if word in words:
            word_has_break[word] = True
            return True

        for i in range(1, len(word)):
            if word[i:] not in words:
                continue
            if self.has_break(word[:i], words, word_has_break):
                word_has_break[word] = True
                return True

        word_has_break[word] = False
        return False

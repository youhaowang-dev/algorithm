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
#
class WordBreak:
    def wordBreak(self, word: str, wordDict: List[str]) -> bool:
        if not word:
            return False
        if not wordDict:
            return True

        end = 0
        return self.search_break(word, set(wordDict), end)

    def search_break(self, word: str, words: Set[str], prev_end: int) -> bool:
        length = len(word)

        if prev_end == length:
            return True

        for end in range(prev_end, length):
            if word[prev_end:end+1] not in words:
                continue

            if self.search_break(word, words, end + 1):
                return True

        return False

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

from ast import List, Set
from collections import deque

# bfs: time n^3 For every starting index, the search can continue till the end of the given string.
# space n for queue size can be up to n
class WordBreak2:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        queue = deque()
        queue.append(0)
        visited = set()

        while queue:
            substring_start = queue.popleft()
            if substring_start in visited:
                continue
            for substring_end in range(substring_start + 1, len(s) + 1):
                if s[substring_start:substring_end] in word_set:
                    queue.append(substring_end)
                    if substring_end == len(s):
                        return True
            visited.add(substring_start)

        return False


# brute force: time O(2^n), split or not split. space: O(n) depth of recrusion tree can go up to n
class WordBreak:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        substring_start = 0
        return self.wordBreakHelper(s, set(wordDict), substring_start)

    def wordBreakHelper(self, s: str, word_dict: Set[str], substring_start: int):
        if substring_start == len(s):
            return True

        for end in range(substring_start + 1, len(s) + 1):
            if s[substring_start:end] in word_dict and self.wordBreakHelper(
                s, word_dict, end
            ):
                return True

        return False


# BFS/DFS
# time n^3, substr operation costs n and totally n^2 substrings
# space n Queue of at most n size is needed.
class WordBreak3:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s or not wordDict:
            return False

        queue = deque()
        queue.append(s)
        seen = set()
        while queue:
            s = queue.popleft()  # for dfs use pop()
            for word in wordDict:
                # check prefix
                if s.startswith(word):
                    rest = s[len(word) :]
                    if rest == "":
                        return True
                    if rest not in seen:
                        queue.append(rest)
                        seen.add(rest)
        return False

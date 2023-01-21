# Hash Table, String, Dynamic Programming, Backtracking, Trie, Memoization
# Amazon 18 Bloomberg 17 Apple 4 Facebook 2 Microsoft 6 Google 3 Snapchat 3 Adobe 2 Audible 2 ByteDance 8 Uber 5 Walmart Global Tech 2 Twitter Dropbox
# https://leetcode.com/problems/word-break-ii/
# Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word
# is a valid dictionary word. Return all such possible sentences in any order.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

# Example 1:
# Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
# Output: ["cats and dog","cat sand dog"]
# Example 2:
# Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
# Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
# Explanation: Note that you are allowed to reuse a dictionary word.
# Example 3:
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: []


from ast import Dict, List, Set

# dfs all substrings with memoization
# time O(n^2) for memoization, totally max n^2 substrings
# without memoization, the time would be O(2^n)
class WordBreakII:
    DELIMITER = " "

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if not s or not wordDict:
            return list()

        substring_to_result = dict()

        return self.build_results(s, set(wordDict), substring_to_result)

    def build_results(
        self, s: str, wordDict: Set[str], substring_to_result: Dict[str, str]
    ):
        # memo return
        if s in substring_to_result:
            return substring_to_result.get(s)

        results = list()
        # exit condition
        if not s:
            return results

        # found a result where entire string is in wordDict
        if s in wordDict:
            results.append(s)

        for substring_end in range(1, len(s)):
            substring = s[:substring_end]
            if substring not in wordDict:
                continue
            # found a result
            rest = s[substring_end:]
            substring_results = self.build_results(rest, wordDict, substring_to_result)
            for substring_result in substring_results:
                results.append(substring + self.DELIMITER + substring_result)
        # add to memo
        substring_to_result[s] = results

        return results

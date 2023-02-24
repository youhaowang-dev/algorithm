# https://leetcode.com/problems/concatenated-words
# Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.

# A concatenated word is defined as a string that is comprised entirely of at least two shorter words (not necesssarily distinct) in the given array.

# Example 1:
# Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
# Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
# Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";
# "dogcatsdog" can be concatenated by "dog", "cats" and "dog";
# "ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
# Example 2:
# Input: words = ["cat","dog","catdog"]
# Output: ["catdog"]

# for each word, split it into prefix and suffix, check both and return
# N is the number of words and L is the max length of a word
# time: O(N * L^3) with memo, O(N * L^2 * 2^L) without memo
# space: O(N*L + L^2) where N*L is for the word set and L^2 for memoization
class ConcatenatedWords:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        if not words:
            return list()

        results = list()
        memo = dict()
        words_set = set(words)
        for word in words:
            if self.is_target(word, words_set, memo):
                results.append(word)

        return results

    def is_target(self, word, words, memo):
        if word in memo:
            return memo[word]

        for i in range(len(word)):
            prefix = word[:i]
            suffix = word[i:]
            if prefix in words:
                if suffix in words:
                    memo[word] = True
                    return True
                if self.is_target(suffix, words, memo):
                    memo[word] = True
                    return True

        memo[word] = False
        return False

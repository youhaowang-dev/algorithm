# Hash Table, String, Breadth-First Search
# Amazon 36 Bloomberg 5 Microsoft 3 LinkedIn 3 Adobe 3 Google 2 Uber 2 Apple 2 Qualtrics 2 PayPay 2 Facebook 12
# Lyft 6 Snapchat 3 Yahoo 2 Walmart Global Tech 2 Box 2 Intel 2 Twilio 2 Zillow 7 Expedia 5 Citadel 5 Salesforce 4
# Hulu 4 VMware 4 Oracle 3 ByteDance 3 Goldman Sachs 3 Nutanix 2 SAP 2 Swiggy 2 Arcesium 2 Yelp
# https://leetcode.com/problems/word-ladder/

# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

# Example 1:
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
# Example 2:
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
from collections import deque
from typing import Deque, List, Set


# breadth first search in a graph where each char of the beginWord can be replaced by a-z(except self)
# if next word in set, continue until the end word is reached
class WordLadder:
    CHARACTERS = "abcdefghijklmnopqrstuvwxyz"

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not wordList:
            return 0

        words = set(wordList)

        if endWord not in words:
            return 0

        queue = deque()
        queue.append(beginWord)

        visited = set()
        visited.add(beginWord)

        distance = 0
        while queue:
            distance += 1
            current_words = self.get_current_words(queue)
            for current_word in current_words:
                if current_word == endWord:
                    return distance

                next_words = self.get_next_words(current_word, words)
                for next_word in next_words:
                    if next_word in visited:
                        continue

                    if next_word in words:
                        queue.append(next_word)
                        visited.add(next_word)

        return 0  # not found

    def get_current_words(self, queue: Deque[str]) -> List[str]:
        words = list()
        while queue:
            words.append(queue.popleft())

        return words

    def get_next_words(self, word: str, words: Set[str]):
        next_words = list()

        word_chars = list(word)
        for i, character in enumerate(word_chars):
            for new_character in self.CHARACTERS:
                if character == new_character:
                    continue

                word_chars[i] = new_character
                new_word = "".join(word_chars)
                next_words.append(new_word)

            word_chars[i] = character

        return next_words

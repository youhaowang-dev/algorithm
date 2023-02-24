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

# BFS for shortest path
class WordLadder:
    LETTERS = "abcdefghijklmnopqrstuvwxyz"

    def ladderLength(self, start_word: str, end_word: str, wordList: List[str]) -> int:
        if not start_word or not end_word or not wordList:
            return 0

        word_set = set(wordList)
        if end_word not in word_set:
            return 0

        queue = deque()
        used = set()
        queue.append(start_word)
        used.add(start_word)
        word_count = 1
        while queue:
            words = self.get_all_words(queue)
            for word in words:
                if word == end_word:
                    return word_count
                else:
                    next_words = self.get_next_words(word, word_set)
                    for next_word in next_words:
                        if next_word in used:
                            continue
                        queue.append(next_word)
                        used.add(next_word)
            word_count += 1

        return 0

    def get_all_words(self, queue):
        words = list()
        while queue:
            words.append(queue.popleft())

        return words

    def get_next_words(self, word, word_set):
        words = list()
        for i, letter in enumerate(word):
            for new_letter in self.LETTERS:
                if letter == new_letter:
                    continue
                new_word = word[:i] + new_letter + word[i+1:]
                if new_word in word_set:
                    words.append(new_word)

        return words

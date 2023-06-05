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
# time O(nm) for hashing
class WordLadder:
    def ladderLength(self, start_word: str, end_word: str, words: List[str]) -> int:
        words = set(words)
        if not words or end_word not in words:
            return 0

        queue = deque()
        visited = set()
        queue.append(start_word)
        visited.add(start_word)
        count = 1
        while queue:
            all_words = self.get_all_words(queue)
            count += 1
            for word in all_words:
                visited.add(word)
                next_words = self.get_next_words(word)
                for next_word in next_words:
                    if next_word == end_word:
                        return count
                    if next_word in visited:
                        continue
                    if next_word in words:
                        queue.append(next_word)
                        visited.add(next_word)

        return 0

    def get_next_words(self, word):
        next_words = list()
        for new_letter in "abcdefghijklmnopqrstuvwxyz":
            for i, old_letter in enumerate(word):
                # if new_letter == old_letter:
                #     continue
                next_words.append(word[:i] + new_letter + word[i + 1:])

        return next_words

    def get_all_words(self, queue):
        words = list()
        while queue:
            words.append(queue.popleft())

        return words


class WordLadderWithPathPrint:
    def ladderLength(self, start: str, end: str, wordList: List[str]) -> int:
        if not start or not end or not wordList:
            return 0
        words = set(wordList)
        if end not in words:
            return 0

        queue = deque()
        word_to_parent = dict()
        queue.append(start)
        word_to_parent[start] = None
        while queue:
            all_words = self.get_all_words(queue)
            for word in all_words:
                next_words = self.get_next_words(word)
                for next_word in next_words:
                    if next_word in word_to_parent:
                        continue
                    if next_word not in words:
                        continue
                    queue.append(next_word)
                    word_to_parent[next_word] = word
                    if next_word == end:
                        return len(self.build_path(end, word_to_parent))

        return 0

    def build_path(self, word, word_to_parent):
        path = deque()
        while word:
            path.appendleft(word)
            word = word_to_parent[word]
        print("->".join(path))
        return path

    def get_all_words(self, queue):
        words = list()
        while queue:
            words.append(queue.popleft())
        return words

    def get_next_words(self, word):
        new_words = list()
        for i, letter in enumerate(word):
            for new_letter in "abcdefghijklmnopqrstuvwxyz":
                # if letter == new_letter:
                #     continue
                new_words.append(word[:i] + new_letter + word[i + 1:])

        return new_words

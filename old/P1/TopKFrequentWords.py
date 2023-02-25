# Hash Table String Trie Sorting Heap (Priority Queue) Bucket Sort Counting
# https://leetcode.com/problems/top-k-frequent-words/
# Given an array of strings words and an integer k, return the k most frequent strings.

# Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

# Example 1:
# Input: words = ["i","love","leetcode","i","love","coding"], k = 2
# Output: ["i","love"]
# Explanation: "i" and "love" are the two most frequent words.
# Note that "i" comes before "love" due to a lower alphabetical order.
# Example 2:
# Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
# Output: ["the","is","sunny","day"]
# Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.


# count, sort, then build result
class TopKFrequentWords:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        result = list()
        if not words:
            return result

        if not k:
            return result

        word_to_count = dict()
        for word in words:
            word_to_count[word] = 1 + word_to_count.get(word, 0)

        word_with_counts = list()
        for word in word_to_count.keys():
            word_with_counts.append((-word_to_count[word], word))
        word_with_counts.sort()

        for _, word in word_with_counts[:k]:
            result.append(word)

        return result

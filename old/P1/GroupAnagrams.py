# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:
# Input: strs = [""]
# Output: [[""]]
# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]

class GroupAnagrams:
    def groupAnagrams(self, words: List[str]) -> List[List[str]]:
        grouped_words = list()
        if not words:
            return grouped_words

        hash_to_words = dict()
        for word in words:
            word_hash = self.get_hash(word)
            if word_hash not in hash_to_words:
                hash_to_words[word_hash] = list()

            hash_to_words[word_hash].append(word)

        for hash in hash_to_words.keys():
            grouped_words.append(hash_to_words[hash])

        return grouped_words

    def get_hash(self, word: str) -> str:
        letters = list(word)
        letters.sort()

        return "".join(letters)
    # counting sort

    def get_hash_lower_case_english_char_only(self, word: str) -> str:
        letters = list(word)
        letter_to_count = dict()
        for letter in letters:
            letter_to_count[letter] = 1 + letter_to_count.get(letter, 0)

        hash = list()
        for letter in "abcdefghijklmnopqrstuvwxyz":
            hash.append(letter)
            count = letter_to_count.get(letter, 0)
            hash.append(str(count))

        return "".join(hash)

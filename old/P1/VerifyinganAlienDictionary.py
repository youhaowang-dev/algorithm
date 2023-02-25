# https://leetcode.com/problems/verifying-an-alien-dictionary/
# In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order.
# The order of the alphabet is some permutation of lowercase letters.

# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and
# only if the given words are sorted lexicographically in this alien language.

# Example 1:
# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
# Example 2:
# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false
# Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
class VerifyinganAlienDictionary:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if not words:
            return True

        letter_to_order_weight = dict()
        for i, letter in enumerate(order):
            letter_to_order_weight[letter] = i

        for i in range(len(words) - 1):
            word = words[i]
            next = words[i + 1]
            if not self.is_sorted(word, next, letter_to_order_weight):
                return False

        return True

    def is_sorted(self, word, next, letter_to_order_weight) -> bool:
        for letter, next_letter in zip(word, next):
            print(letter, next_letter, letter_to_order_weight.get(
                letter, 0), letter_to_order_weight.get(next_letter, 0))
            if letter != next_letter:
                return letter_to_order_weight.get(letter, 0) <= letter_to_order_weight.get(next_letter, 0)

        return len(word) <= len(next)

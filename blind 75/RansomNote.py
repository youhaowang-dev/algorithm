# Hash Table, String, Counting
# https://leetcode.com/problems/ransom-note/
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters
# from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true


class RansomNote:
    def canConstruct(self, target: str, word: str) -> bool:
        if not word:
            return False
        if not target:
            return True

        letter_to_count = dict()
        for letter in word:
            letter_to_count[letter] = 1 + letter_to_count.get(letter, 0)

        for letter in target:
            if letter not in letter_to_count:
                return False

            letter_to_count[letter] -= 1
            if letter_to_count[letter] < 0:
                return False

        return True

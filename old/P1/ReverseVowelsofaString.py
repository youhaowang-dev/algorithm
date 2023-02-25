# Two Pointers, String
# Apple 3 Bloomberg 3 Yahoo 3 Uber 2 Google 4 Facebook 4 Amazon 4 Adobe 2

# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

# Example 1:
# Input: s = "hello"
# Output: "holle"

# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"

# two pointers
class ReverseVowelsofaString:
    VOWELS = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    def reverseVowels(self, s: str) -> str:
        characters = list(s)
        left = 0
        right = len(characters) - 1
        while left < right:
            while left < right and characters[right] not in self.VOWELS:
                right -= 1
            while left < right and characters[left] not in self.VOWELS:
                left += 1

            if left < right:
                (characters[left], characters[right]) = (
                    characters[right],
                    characters[left],
                )
                left += 1
                right -= 1

        return "".join(characters)

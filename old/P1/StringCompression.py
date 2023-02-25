# Two Pointers, String
# Apple 4 Expedia 3 Facebook 2 Goldman Sachs 2 Amazon 2 Redfin 2 Google 2 Microsoft 10 Yandex 6 Bloomberg 4 Yahoo 3
# instacart 3 Visa 2 Twitter 2 eBay 4 IBM 4 Nvidia 4 Adobe 3 Nutanix 2 Oracle 2 VMware 2 Cisco 2 GoDaddy Snapchat Yelp Lyft
# https://leetcode.com/problems/string-compression/

# Given an array of characters chars, compress it using the following algorithm:

# Begin with an empty string s. For each group of consecutive repeating characters in chars:

# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, be stored in the input character array chars.
# Note that group lengths that are 10 or longer will be split into multiple characters in chars.
# After you are done modifying the input array, return the new length of the array.
# You must write an algorithm that uses only constant extra space.

# Example 1:
# Input: chars = ["a","a","b","b","c","c","c"]
# Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
# Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".


from ast import List


class StringCompression:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0

        insert_index = 1
        char_count = 1
        prev_char = chars[0]
        for i in range(1, len(chars)):
            if prev_char == chars[i]:
                char_count += 1
            else:
                # found different char
                insert_index = self.append_chars(char_count, chars, insert_index)
                chars[insert_index] = chars[i]
                insert_index += 1
                char_count = 1
                prev_char = chars[i]

        insert_index = self.append_chars(char_count, chars, insert_index)

        return insert_index

    def append_chars(self, char_count, chars, insert_index):
        if 10 > char_count > 1:
            chars[insert_index] = str(char_count)
            insert_index += 1
        if char_count >= 10:
            for char in str(char_count):
                chars[insert_index] = char
                insert_index += 1

        return insert_index

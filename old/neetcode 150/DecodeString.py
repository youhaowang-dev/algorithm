# https://leetcode.com/problems/decode-string/description/
# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated
# exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; there are no extra white spaces, square brackets are
# well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits
# are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

# The test cases are generated so that the length of the output will never exceed 105.

# Example 1:
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# Example 2:
# Input: s = "3[a2[c]]"
# Output: "accaccacc"
# Example 3:
# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"

class DecodeString:
    def decodeString(self, s: str) -> str:
        if not s:
            return ""

        stack = deque()
        for i, letter in enumerate(s):
            if letter != "]":
                stack.append(letter)
                continue
            # == ], so process the stack until [
            string = self.get_string(stack)
            string_count = self.get_string_count(stack)
            stack.append(string_count * string)

        return "".join(stack)

    def get_string(self, stack) -> str:
        string = ""
        # everything before [ is the string part
        while stack and stack[-1] != "[":
            string = stack.pop() + string
        stack.pop()  # del the "["

        return string

    def get_string_count(self, stack) -> int:
        count = ""
        while stack and stack[-1].isdigit():
            count = stack.pop() + count

        return int(count)

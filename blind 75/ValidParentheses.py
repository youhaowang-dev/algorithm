# String, Stack
# https://leetcode.com/problems/valid-parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Example 1:
# Input: s = "()"
# Output: true
# Example 2:
# Input: s = "()[]{}"
# Output: true
# Example 3:
# Input: s = "(]"
# Output: false

# map open to close, push open in stack, pop open when having a close and compare with the expected close
class ValidParentheses:
    OPEN_TO_CLOSE = {
        "(": ")",
        "[": "]",
        "{": "}",
    }

    def isValid(self, letters: str) -> bool:
        if not letters:
            return True

        closes = self.OPEN_TO_CLOSE.values()
        stack = deque()
        for letter in letters:
            if letter in self.OPEN_TO_CLOSE:
                stack.append(letter)
            elif letter in closes:
                if not stack:
                    return False  # input like ")"
                expected_close = self.OPEN_TO_CLOSE[stack.pop()]
                if expected_close != letter:
                    return False
            else:
                pass

        return not stack  # should not have leftover

# https://leetcode.com/problems/regular-expression-matching/description/
# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).


# Example 1:

# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:

# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
# Example 3:

# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
class RegularExpressionMatching:
    def isMatch(self, s: str, p: str) -> bool:
        memo = dict()
        return self.search_match(s, 0, p, 0, memo)

    def search_match(self, s, s_index, p, p_index, memo):
        if (s_index, p_index) in memo:
            return memo[(s_index, p_index)]
        if s_index >= len(s) and p_index >= len(p):
            return True
        if p_index >= len(p):
            return False

        is_match = s_index < len(s) and (
            s[s_index] == p[p_index] or "." == p[p_index])
        if p_index + 1 < len(p) and p[p_index + 1] == "*":
            has_match = self.search_match(s, s_index, p, p_index + 2, memo) or (
                is_match and self.search_match(s, s_index + 1, p, p_index, memo))  # skip * or (match and use *)
            memo[(s_index, p_index)] = has_match
            return has_match

        if is_match:
            has_match = self.search_match(s, s_index + 1, p, p_index + 1, memo)
            memo[(s_index, p_index)] = has_match
            return has_match

        return False

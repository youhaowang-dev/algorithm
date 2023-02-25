# https://leetcode.com/problems/generate-parentheses/
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:
# Input: n = 1
# Output: ["()"]
class GenerateParentheses:
    def generateParenthesis(self, n: int) -> List[str]:
        results = list()
        if not n:
            return results

        result = list()
        left_count = 0
        right_count = 0
        self.build_results(n, results, result, left_count, right_count)

        return results

    def build_results(self, n, results, result, left_count, right_count):
        if left_count == n and right_count == n:
            results.append("".join(result))

        if left_count < n:
            result.append("(")
            self.build_results(n, results, result, left_count + 1, right_count)
            result.pop()
        if left_count > right_count:
            result.append(")")
            self.build_results(n, results, result, left_count, right_count + 1)
            result.pop()

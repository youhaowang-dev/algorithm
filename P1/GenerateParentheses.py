# String, Dynamic Programming, Backtracking
# Amazon 16 Adobe 6 Apple 5 Microsoft 4 TikTok 4 Bloomberg 3 Uber 2 Google 2 Lyft 2 Yahoo 2 Walmart Global Tech 2
# Yandex 2 Oracle 2 Infosys 2 TripAdvisor 2 Facebook 17 C3 IoT 4 ServiceNow 3 ByteDance 3 Huawei 3 Zoho 3
# Salesforce 2 Grab 2 Intuit 3 Goldman Sachs 3 Paypal 3 tcs 3 eBay 2 Nvidia 2 Snapchat 2 Spotify 2 Wish 2
# FactSet 2 Zoom 2 Arcesium 2 razorpay 2 Tesla 2 Zenefits
# https://leetcode.com/problems/generate-parentheses/

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:
# Input: n = 1
# Output: ["()"]
from ast import List


class GenerateParentheses:
    LEFT = "("
    RIGHT = ")"

    def generateParenthesis(self, n: int) -> List[str]:
        result = list()
        if n == 0:
            return result

        result_state = ""
        left_count = n
        right_count = n
        self.build_result(left_count, right_count, result, result_state)

        return result

    def build_result(self, left_count, right_count, result, result_state):
        if right_count < left_count:
            return

        if right_count < 0 or left_count < 0:
            return

        if not left_count and not right_count:
            result.append(result_state)
            return

        self.build_result(left_count - 1, right_count, result, result_state + self.LEFT)
        self.build_result(
            left_count, right_count - 1, result, result_state + self.RIGHT
        )

    def build_result2(self, left_count, right_count, result, result_state):
        if right_count < left_count:
            return

        if not left_count and not right_count:
            result.append(result_state)
            return

        if left_count:
            self.build_result2(
                left_count - 1, right_count, result, result_state + self.LEFT
            )
        if right_count:
            self.build_result2(
                left_count, right_count - 1, result, result_state + self.RIGHT
            )

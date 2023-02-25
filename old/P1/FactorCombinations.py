# Array, Backtracking
# LinkedIn 3 TikTok 2 Uber
# https://leetcode.com/problems/factor-combinations/
# Numbers can be regarded as the product of their factors.

# For example, 8 = 2 x 2 x 2 = 2 x 4.
# Given an integer n, return all possible combinations of its factors. You may return the answer in any order.

# Note that the factors should be in the range [2, n - 1].

# Example 1:
# Input: n = 1
# Output: []
# Example 2:
# Input: n = 12
# Output: [[2,6],[3,4],[2,2,3]]
# Example 3:
# Input: n = 37
# Output: []
from ast import List

# time O(n^(1.5)) where O(n) total solutions and each solution costs O(n^(0.5)) to find
# space O(log(n)) where the length of each solution is bound by O(log(n))
# The length of each solution is on the order of O(log⁡(n))
# getFactors(12)
# result_state=[]       n=12    divisor_start=2
# result_state=[2]      n=6     divisor_start=2
# result_state=[2, 2]   n=3     divisor_start=2
# result_state=[3]      n=4     divisor_start= 3
class FactorCombinations:
    def getFactors(self, n: int) -> List[List[int]]:
        results = list()
        if n <= 3:
            return results

        result_state = list()
        divisor_start = 2  # don't want to divide the number by 1, you always want to start dividing by 2.
        self.build_results(n, divisor_start, results, result_state)
        return results

    def build_results(self, n, divisor_start, results, result_state):
        # for divisor in range(divisor_start, n): # TLE
        for divisor in range(divisor_start, int(n**0.5) + 1):
            divide_result, remain = divmod(n, divisor)
            # The previous factor is no bigger than the next
            if remain == 0 and divide_result >= divisor:
                result_state.append(divisor)
                result = list(result_state)
                result.append(divide_result)
                results.append(result)
                self.build_results(divide_result, divisor, results, result_state)
                result_state.pop()

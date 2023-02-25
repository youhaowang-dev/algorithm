# https://leetcode.com/problems/combination-sum-iii/
# Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

# Only numbers 1 through 9 are used.
# Each number is used at most once.
# Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

# Example 1:
# Input: k = 3, n = 7
# Output: [[1,2,4]]
# Explanation:
# 1 + 2 + 4 = 7
# There are no other valid combinations.
# Example 2:
# Input: k = 3, n = 9
# Output: [[1,2,6],[1,3,5],[2,3,4]]
# Explanation:
# 1 + 2 + 6 = 9
# 1 + 3 + 5 = 9
# 2 + 3 + 4 = 9
# There are no other valid combinations.

# time O(9*2^9) => O(1) as max number is 9 and max count is 9, copy takes O(9)
# space O(9 + 9) for recursion depth and  => O(1) if not considering the output
class Solution:
    def combinationSum3(self, count: int, target_sum: int) -> List[List[int]]:
        if not count or not target_sum:
            return list()

        results = list()
        result = list()
        start_num = 1
        self.build_results(results, result, target_sum, count, start_num)

        return results

    def build_results(self, results, result, target_sum, count, start_num):
        if len(result) == count:
            if target_sum == 0:
                results.append(list(result))

            return

        for num in range(start_num, 10):
            result.append(num)
            self.build_results(
                results, result, target_sum - num, count, num + 1)
            result.pop()

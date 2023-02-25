# Given an integer array nums, return all the different possible non-decreasing subsequences of
# the given array with at least two elements. You may return the answer in any order.

# Example 1:
# Input: nums = [4,6,7,7]
# Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
# Example 2:
# Input: nums = [4,4,3,2,1]
# Output: [[4,4]]

from ast import List

# dfs time O(n*n^2) space
# space O(n*2^n) The answer contains O(2^n) sequences, each having a length of O(n).
# If we do not count the answer as part of the space complexity, then the space complexity is O(n)
# for the recursion call stack and space needed to build each sequence.
# [1,1,1,2] => [[1,1],[1,1,1],[1,1,1,2],[1,1,2],[1,2]]
# [], [1], [1, 1], [1, 1, 1], [1, 1, 1, 2], [1, 1, 2], [1, 2], [2]
# [1,2,1,2] => [[1,2],[1,2,2],[1,1],[1,1,2],[2,2]]
# [], [1], [1, 2], [1, 2, 2], [1, 1], [1, 1, 2], [2], [2, 2]
class NondecreasingSubsequences:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        results = list()
        if not nums:
            return results

        result_state = list()
        start_index = 0
        self.build_results(nums, start_index, result_state, results)

        return results

    def build_results(self, nums, start_index, result_state, results):
        if len(result_state) >= 2:
            results.append(list(result_state))

        visited = set()
        for i in range(start_index, len(nums)):
            if nums[i] in visited:
                continue

            visited.add(nums[i])
            if not result_state or nums[i] >= result_state[-1]:
                result_state.append(nums[i])
                self.build_results(nums, i + 1, result_state, results)
                result_state.pop()

# Array, Backtracking
# Airbnb 4 Reddit 4 Amazon 2 Facebook 5 Bloomberg 4 Google 2 Microsoft 2 Oracle 2 ByteDance 2 Uber 3 eBay 3
# LinkedIn 2 Apple 2 TikTok 2 Snapchat
# https://leetcode.com/problems/combination-sum-ii/

# Given a collection of candidate numbers (candidates) and a target number (target),
# find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.

# Example 1:
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# Example 2:
# Input: candidates = [2,5,2,1,2], target = 5
# Output:
# [
# [1,2,2],
# [5]
# ]
from ast import List

# Time complexity is O(2^n). Space complexity O(n). For each num you have two choices, pick it or not.
class CombinationSumII:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        result = list()
        if not nums:
            return result

        list_state = list()
        start_index = 0
        # Sort removes dups, for example, 1,2a,2b,5, to get 7,
        # cur pointer is on 1, then 1, 2a, 5, and 1, 2b, 5, would be dups.
        # select multi values, for example 1,2,2, it will be covered when cur pointer is 2a
        self.combinationSum2Helper(
            sorted(nums), target, list_state, start_index, result
        )

        return result

    def combinationSum2Helper(self, nums, target, list_state, start_index, result):
        if target < 0:
            return

        if target == 0:
            result.append(list(list_state))
            return

        # target > 0
        for i in range(start_index, len(nums)):
            # dedup
            # i > startIndex is for NOT skipping the first number as it should always be picked
            # i > startIndex also handles edge cases where i == 0
            if i > start_index and nums[i] == nums[i - 1]:
                continue

            list_state.append(nums[i])
            self.combinationSum2Helper(
                nums, target - nums[i], list_state, i + 1, result
            )
            list_state.pop()

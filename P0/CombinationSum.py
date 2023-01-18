# Array, Backtracking
# Airbnb 9 Amazon 5 eBay 4 Google 3 Adobe 3 Microsoft 3 Apple 3 Facebook 2 Walmart Global Tech 2 Reddit 2
# Bloomberg 9 ByteDance 5 LinkedIn 4 Goldman Sachs 2 Zillow 2 Oracle 2 TikTok 2 Snapchat 4 Uber 4 Salesforce 3 Cisco 2 Arcesium 2
# https://leetcode.com/problems/combination-sum/

# Given an array of distinct integers candidates and a target integer target, return a list of all unique
# combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
# frequency
#  of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

# Example 1:
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# Example 2:
# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
# Example 3:
# Input: candidates = [2], target = 1
# Output: []

# time O(nums_count^(target/min_num)) => O(N^(T/M))
# each number will fanout O(target/min_num) searches recursively, and each search cost bounded by O(nums_count)
# space O(target/min_num)
from ast import List


class CombinationSum:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = list()
        if not nums:
            return result

        list_state = list()
        start_index = 0
        target_remain = target - 0
        self.combinationSumHelper(nums, target_remain, start_index, list_state, result)

        return result

    def combinationSumHelper(
        self, nums, target_remain, start_index, list_state, result
    ):
        if target_remain < 0:
            return

        if target_remain == 0:
            result.append(list(list_state))

        # target_remain > 0
        for i in range(start_index, len(nums)):
            list_state.append(nums[i])
            # no i + 1 for reuse the number
            self.combinationSumHelper(
                nums, target_remain - nums[i], i, list_state, result
            )
            list_state.pop()

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

# time O(n*2^n) where n=target/min_num, each num can be picked n times and choices are 2(pick/not pick). copy takes n
# so TC can be O(n*2^target) as min_num can be 1
# space O(target/min_num) = O(target) where min_num can be 1
class CombinationSum:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return list()

        results = list()
        result = list()
        start = 0  # we don't go backward to produce [2,3,2]
        self.build_results(nums, results, result, target, start)

        return results

    def build_results(self, nums, results, result, target, start):
        if target == 0:
            results.append(list(result))
            return
        if target < 0:
            return

        for i in range(start, len(nums)):
            result.append(nums[i])
            self.build_results(nums, results, result, target - nums[i], i)
            result.pop()

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

# time O(n*2^n) where n=target/min_num=max_picks, For each num you have two choices, pick it or not. copy takes n
# space O(n) for recursion depth and hash table and output
class CombinationSumII:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return list()

        num_to_count = collections.Counter(nums)
        results = list()
        result = list()
        unique_nums = list(num_to_count.keys())
        start = 0
        self.build_results(results, result, target,
                           num_to_count, unique_nums, start)

        return results

    def build_results(self, results, result, target, num_to_count, nums, start):
        if target == 0:
            results.append(list(result))
            return

        if target < 0:
            return

        for i in range(start, len(nums)):
            num = nums[i]
            if num_to_count[num] == 0:
                continue

            result.append(num)
            num_to_count[num] -= 1
            self.build_results(results, result, target -
                               num, num_to_count, nums, i)
            result.pop()
            num_to_count[num] += 1

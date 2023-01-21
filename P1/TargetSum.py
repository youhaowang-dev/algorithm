# Array, Dynamic Programming, Backtracking
# Amazon 6 Facebook 5 Uber 3 Apple 2 Bloomberg 2 Yahoo 2 Adobe 6 Google 3 Microsoft 3 McKinsey 3 ByteDance 2 SAP 2
# https://leetcode.com/problems/target-sum/
# You are given an integer array nums and an integer target.

# You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
# Return the number of different expressions that you can build, which evaluates to target.

# Example 1:
# Input: nums = [1,1,1,1,1], target = 3
# Output: 5
# Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3
# Example 2:
# Input: nums = [1], target = 1
# Output: 1


from ast import List
from collections import defaultdict

# bfs to build the result_to_count, return result_to_count[target_result]
# time n space n where n is len(nums)
# [1,1,1] target_result=1 expect 3, 1+1-1, 1-1+1, -1+1+1
# {0: 1} => {1: 1, -1: 1} => {2: 1, 0: 2, -2: 1} => {3: 1, 1: 3, -1: 3, -3: 1}
class TargetSum:
    def findTargetSumWays(self, nums: List[int], target_result: int) -> int:
        if not nums:
            return 0

        result_to_count = defaultdict(int)
        result_to_count[0] = 1
        for num in nums:
            next_result_to_count = defaultdict(int)
            for result in result_to_count.keys():
                # do + and -
                next_result_to_count[result + num] += result_to_count[result]
                next_result_to_count[result - num] += result_to_count[result]
            result_to_count = next_result_to_count

        return result_to_count[target_result]

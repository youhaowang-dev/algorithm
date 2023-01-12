# Array, Binary Search, Sliding Window, Prefix Sum
# Apple 3 Citadel 3 Amazon 2 Microsoft 2 Facebook 6 Bloomberg 3 Goldman Sachs 3 Google 3 Adobe 2 Yahoo 2 Arcesium 2
# https://leetcode.com/problems/minimum-size-subarray-sum/
# Given an array of positive integers nums and a positive integer target, return the minimal length of a
# subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

# Example 1:
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Example 2:
# Input: target = 4, nums = [1,4,4]
# Output: 1
# Example 3:
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0


from typing import List


class MinimumSizeSubarraySum:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0

        left = 0
        right = 0
        sum = 0
        min_subarr_length = float("inf")
        while right < len(nums):
            sum = sum + nums[right]
            right += 1

            while sum >= target:
                # right is now at the right bound + 1 position of the valid range
                subarr_length = right - left  # right-1 - left + 1 = right - left
                min_subarr_length = min(min_subarr_length, subarr_length)
                sum = sum - nums[left]
                left += 1

        if min_subarr_length == float("inf"):
            return 0

        return min_subarr_length

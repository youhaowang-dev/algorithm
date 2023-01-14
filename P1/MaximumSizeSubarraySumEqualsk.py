# Array, Hash Table, Prefix Sum
# Apple 2 Facebook 6 Amazon 2 Microsoft 3 Goldman Sachs 3 Palantir Technologies
# https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/
# Given an integer array nums and an integer k, return the maximum length of a subarray that sums to k.
# If there is not one, return 0 instead.

# Example 1:
# Input: nums = [1,-1,5,-2,3], k = 3
# Output: 4
# Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.

# Example 2:
# Input: nums = [-2,-1,2,1], k = 1
# Output: 2
# Explanation: The subarray [-1, 2] sums to 1 and is the longest.

from typing import List

# brute force: try all subarrays

# prefix sum
# if there exists some subarray from i to j summing to target in nums, then we know that
# prefixSum[j] - prefixSum[i] = target => prefixSum[j] - target = prefixSum[i]
class MaximumSizeSubarraySumEqualsk:
    def maxSubArrayLen(self, nums: List[int], target: int) -> int:
        max_subarray_length = 0
        if not nums:
            max_subarray_length

        prefix_sum = 0
        prefix_sum_to_index = dict()
        for i, num in enumerate(nums):
            prefix_sum += num

            if prefix_sum == target:
                max_subarray_length = i + 1

            prev_prefix_sum = prefix_sum - target
            if prev_prefix_sum in prefix_sum_to_index:
                max_subarray_length = max(
                    max_subarray_length, i - prefix_sum_to_index.get(prev_prefix_sum)
                )

            if prefix_sum not in prefix_sum_to_index:
                prefix_sum_to_index[prefix_sum] = i

        return max_subarray_length

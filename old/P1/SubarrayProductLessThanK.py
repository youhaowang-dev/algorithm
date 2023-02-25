# Array, Sliding Window
# Facebook 3 Amazon 3 LinkedIn 7 Bloomberg 4 Goldman Sachs 2 Uber 2 Walmart Global Tech 2 Microsoft 2 Yatra
# https://leetcode.com/problems/subarray-product-less-than-k/

# Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

# Example 1:
# Input: nums = [10,5,2,6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
# Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

# Example 2:
# Input: nums = [1,2,3], k = 0
# Output: 0

from typing import List

# two pointers O(2n)
# [1,2,3,4] k = 100
# [] -> [] // Step 0, 0 subarrays, left=0 right=0
# [1] -> [1] // Step 1, 1 subarrays, left=0 right=1
# [1,2] -> [1,2],[1],[2] // Step 2. 3 subarrays,left=0 right=2
# [1,2,3] -> [1,2],[1],[2],[1,2,3],[2,3],[3] // Step 3. 4 subarrays,left=0 right=3
# [1,2,3,4] -> [1,2],[1],[2],[1,2,3],[2,3],[3],[1,2,3,4],[2,3,4],[3,4],[4] // Step 4, 10 subarrays, left=0 right=3
# 10 = 4 + 3 + 2 + 1 = sum(left - right + 1)
class SubarrayProductLessThanK:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = 0

        current_prod = 1
        left = 0
        for right in range(0, len(nums)):
            current_prod *= nums[right]

            while left <= right and current_prod >= k:
                current_prod //= nums[left]
                left += 1

            count += right - left + 1

        return count

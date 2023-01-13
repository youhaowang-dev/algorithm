# Array, Design, Prefix Sum
# Facebook 3 Adobe 4 Amazon 2 Palantir Technologies
# https://leetcode.com/problems/range-sum-query-immutable/description/

# Given an integer array nums, handle multiple queries of the following type:

# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:

# NumArray(int[] nums) Initializes the object with the integer array nums.
# int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).


# Example 1:

# Input
# ["NumArray", "sumRange", "sumRange", "sumRange"]
# [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
# Output
# [null, 1, -1, -3]

# Explanation
# NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
# numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
# numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
# numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3

from typing import List

# brute force: calculate at request time

# because immutable, prefix sum can be used
class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix_sum = self.get_prefix_sum(nums)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right + 1] - self.prefix_sum[left + 1 - 1]

    def get_prefix_sum(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix_sum = [0 for _ in range(0, length + 1)]
        for i in range(0, length):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        return prefix_sum

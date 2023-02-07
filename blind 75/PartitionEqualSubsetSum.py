# https://leetcode.com/problems/partition-equal-subset-sum/
# Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the
# elements in both subsets is equal or false otherwise.

# Example 1:
# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# Example 2:
# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.

# brute force: for each element of the array, we can either place it in 1st subset, or place it in 2nd subset.
# time 2^n, space n
class PartitionEqualSubsetSum:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums:
            return False

        sum1 = 0
        sum2 = 0
        return self.can_partition(nums, 0, sum1, sum2)

    def can_partition(self, nums, i, sum1, sum2):
        if i == len(nums):
            return sum1 == sum2

        next_index = i + 1
        next_num = nums[i]
        can_partition1 = self.can_partition(
            nums, next_index, sum1 + next_num, sum2)
        can_partition2 = self.can_partition(
            nums, next_index, sum1, sum2 + next_num)

        return can_partition1 or can_partition2

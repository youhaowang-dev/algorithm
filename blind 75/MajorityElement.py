# Array, Hash Table, Divide and Conquer, Sorting, Counting
# https://leetcode.com/problems/majority-element/
# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Example 1:
# Input: nums = [3,2,3]
# Output: 3
# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

# brute force: sort and return len // 2
# count number, time O(n) space O(n)
class MajorityElement:
    def majorityElement(self, nums: List[int]) -> int:
        # if not nums:
        num_to_count = dict()
        for num in nums:
            num_to_count[num] = 1 + num_to_count.get(num, 0)

        for num, count in num_to_count.items():
            if count > len(nums) // 2:
                return num

        return 0  # raise Exception("no major")

# 摩尔投票算法: 抵消两个不同得数，剩下无法抵消的就是众数，这个基于众数一定存在的假设
# modify input by updating different number pair to an impossible value
# two pointers
class MajorityElement2:
    def majorityElement(self, nums: List[int]) -> int:
        left = 0
        right = 1
        while right < len(nums):
            if nums[left] == None:
                left += 1
            elif nums[left] == nums[right]:
                right += 1
            else:
                nums[left] = None
                nums[right] = None
                left += 1
                right += 1
        for num in nums:
            if num:
                return num

        raise Exception("no major number")

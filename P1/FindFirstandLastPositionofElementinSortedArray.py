# Array, Binary Search
# Amazon 15 Facebook 9 Adobe 6 Bloomberg 5 Apple 4 Intuit 4 LinkedIn 2 Uber 2 Google 2 Samsung 2 Microsoft 10 Yahoo 2 Qualtrics 2 Oracle 2 SAP 2 ByteDance 5 Nutanix 3 Twitter 3 Yandex 2 Splunk 2 Citadel 2 Dell 2 TikTok 2 instacart 2
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Given an array of integers nums sorted in non-decreasing order, find the lefting and righting position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:
# Input: nums = [], target = 0
# Output: [-1,-1]


# brute force
# Given a target element, we can simply do a linear scan over the entire array to find the first and
# the last position. The first occurrence will be the first time when we encounter this target. Thereafter,
# we continue to scan elements until we find one that is greater than the target or until we reach the
# end of the array. This will help us determine the last position of the target.

from ast import List
from enum import Enum


class SearchType(Enum):
    FIND_FIRST = 1
    FIND_LAST = 2


class FindFirstandLastPositionofElementinSortedArray:
    def searchRange(self, nums: List[int], target: int):
        if len(nums) == 0:
            return [-1, -1]

        first = self.find_position(nums, target, SearchType.FIND_FIRST)
        last = self.find_position(nums, target, SearchType.FIND_LAST)
        if first == -1 or last == -1:
            return [-1, -1]

        return [first, last]

    def find_position(
        self, nums: List[int], target: int, searchType: SearchType
    ) -> int:
        if nums is None or len(nums) == 0:
            return -1

        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            midVal = nums[mid]
            if midVal == target:
                # 1,1,1,1,1
                # l     m     r
                if searchType == SearchType.FIND_FIRST:
                    right = mid

                if searchType == SearchType.FIND_LAST:
                    left = mid

            if midVal < target:
                left = mid

            if midVal > target:
                right = mid

        # left==right or left+1==right
        if searchType == SearchType.FIND_FIRST:
            if nums[left] == target:
                return left

            if nums[right] == target:
                return right

        if searchType == SearchType.FIND_LAST:
            if nums[right] == target:
                return right

            if nums[left] == target:
                return left

        return -1


class FindFirstandLastPositionofElementinSortedArray2:
    # bianry search O(logn)
    # find first and last by binary search move left and right differently when midVal==target
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums is None or len(nums) == 0:
            return [-1, -1]

        first = self.find_first_position(nums, target)
        last = self.find_last_position(nums, target)
        if first == -1 or last == -1:
            return [-1, -1]

        return [first, last]

    def find_first_position(self, nums: List[int], target: int) -> int:
        if nums is None or len(nums) == 0:
            return -1

        left = 0
        right = len(nums) - 1
        # left+1<right guarantees no infinite loop
        while left + 1 < right:
            mid = (left + right) // 2
            midVal = nums[mid]
            if midVal == target:
                right = mid  # drop the right part for searching the first position

            if midVal > target:
                right = mid

            if midVal < target:
                left = mid

        # handle end states
        # check left bound first
        if nums[left] == target:
            return left

        if nums[right] == target:
            return right

        return -1

    def find_last_position(self, nums: List[int], target: int) -> int:
        if nums is None or len(nums) == 0:
            return -1

        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            midVal = nums[mid]
            if midVal == target:
                left = mid  # drop the left part for searching the last position

            if midVal > target:
                right = mid

            if midVal < target:
                left = mid

        # check right bound first
        if nums[right] == target:
            return right

        if nums[left] == target:
            return left

        return -1

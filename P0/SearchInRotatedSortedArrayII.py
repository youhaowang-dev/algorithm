# Array, Binary Search
# Amazon 3 LinkedIn 5 Facebook 3 Adobe 3 Apple 2 Microsoft 3 Google 2 TikTok 2
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/

# This problem is similar to Search in Rotated Sorted Array, but nums may contain duplicates.
# Would this affect the runtime complexity? How and why?

# There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).
# Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < len(nums)) such that
# the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
# For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].
# Given the array nums after the rotation and an integer target, return True if target is in nums, or False if it is not in nums.
# You must decrease the overall operation steps as much as possible.

# brute force: O(n) linear scan

from typing import List


class SearchInRotatedSortedArrayII:
    # O(n)
    # with duplicates, mid cannot be (left+right)//2 as the duplicate length is unknown
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False

        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            mid_val = nums[mid]
            left_val = nums[left]
            right_val = nums[right]
            # handle equals
            if mid_val == target:
                return True

            if left_val == target:
                return True

            if right_val == target:
                return True

            # handle duplicate
            if left_val == mid_val:
                left += 1
                continue

            if mid_val == right_val:
                right -= 1
                continue

            # left is sorted
            left_part_sorted = left_val < mid_val
            target_in_left_part = left_val < target and target < mid_val
            if left_part_sorted:
                if target_in_left_part:
                    right = mid
                else:
                    left = mid

            # right is sorted
            right_part_sorted = mid_val < right_val
            target_in_right_part = mid_val < target and target < right_val
            if right_part_sorted:
                if target_in_right_part:
                    left = mid
                else:
                    right = mid

        return nums[left] == target or nums[right] == target


class SearchInRotatedSortedArrayII2:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return False

        search = BinarySearchTarget(nums, target)
        while search.unfinished():
            if search.found_target():
                return True

            if search.foundDuplicate():
                search.handle_duplicate()
                continue

            search.update_left_part()
            search.update_right_part()

        return search.found_target()


class BinarySearchTarget:
    def __init__(self, nums: List[int], target: int):
        self.left = 0
        self.right = len(nums) - 1
        self.target = target
        self.nums = nums

    def unfinished(self) -> bool:
        return self.left + 1 < self.right

    def found_target(self) -> bool:
        return (
            self.get_mid_val() == self.target
            or self.get_left_val() == self.target
            or self.get_right_val() == self.target
        )

    def foundDuplicate(self) -> bool:
        return self.left_has_duplicate() or self.right_has_duplicate()

    def left_has_duplicate(self) -> bool:
        return self.get_left_val() == self.get_mid_val()

    def right_has_duplicate(self) -> bool:
        return self.get_right_val() == self.get_mid_val()

    def handle_duplicate(self) -> None:
        if self.left_has_duplicate():
            self.left += 1

        if self.right_has_duplicate():
            self.right -= 1

    def update_left_part(self) -> None:
        if self.left_part_sorted():
            if self.target_in_left_part():
                self.right = self.get_mid()
            else:
                self.left = self.get_mid()

    def update_right_part(self) -> None:
        if self.right_part_sorted():
            if self.target_in_right_part():
                self.left = self.get_mid()
            else:
                self.right = self.get_mid()

    def get_left_val(self) -> int:
        return self.nums[self.left]

    def get_right_val(self) -> int:
        return self.nums[self.right]

    def get_mid_val(self) -> int:
        return self.nums[self.get_mid()]

    def get_mid(self) -> int:
        return self.left + (self.right - self.left) // 2

    def left_part_sorted(self) -> bool:
        return self.get_left_val() < self.get_mid_val()

    def target_in_left_part(self) -> bool:
        return self.get_left_val() < self.target and self.target < self.get_mid_val()

    def right_part_sorted(self) -> bool:
        return self.get_mid_val() < self.get_right_val()

    def target_in_right_part(self) -> bool:
        return self.get_mid_val() < self.target and self.target < self.get_right_val()

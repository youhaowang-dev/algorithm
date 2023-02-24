# Array, Binary Search, Divide and Conquer
# Amazon 21 Bloomberg 10 Microsoft 7 Apple 7 Adobe 5 Media.net 5 Facebook 4 LinkedIn 4 Uber 3 Yahoo 2 Google 2 TikTok 2
# https://leetcode.com/problems/search-in-rotated-sorted-array/
# There is an integer array nums sorted in ascrighting order (with distinct values).
# Prior to being passed to your function, nums is possibly rotated at an unknown pivot
# index k (1 <= k < len(nums)) such that the resulting array is
# [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
# For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums,
# or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:
# Input: nums = [1], target = 0
# Output: -1


# brute force: linear scan O(n)
# at least one of [left, mid] and [mid, right] will be sorted, check if target in them
# binary search O(logn)
class SearchInRotatedSortedArray:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            if nums[left] == target:  # so dont need to handle == later
                return left
            if nums[right] == target:
                return right
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # one or two sorted parts will exist
            if nums[left] < nums[mid]:
                if nums[left] < target < nums[mid]:
                    right = mid
                else:
                    left = mid
            if nums[mid] < nums[right]:
                if nums[mid] < target < nums[right]:
                    left = mid
                else:
                    right = mid

        if nums[left] == target:
            return left

        if nums[right] == target:
            return right

        return -1

# 1. binary search the min index
# 2. binary search the target in the sorted part


class SearchInRotatedSortedArray3:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        minIndex = self.find_min_index(nums)
        # if min is -1, that means the array is not rotated, the following code still works
        rightVal = nums[len(nums) - 1]
        if target == rightVal:
            return len(nums) - 1

        targetInLeftPart = target > rightVal
        left = 0 if targetInLeftPart else minIndex
        right = minIndex - 1 if targetInLeftPart else len(nums) - 1
        while left + 1 < right:
            mid = left - (left - right) // 2
            midVal = nums[mid]
            if midVal == target:
                return mid
            if midVal < target:
                left = mid
            if midVal > target:
                right = mid

        # if not found, index could go out of bound
        if left >= 0 and left <= len(nums) - 1 and nums[left] == target:
            return left
        if right >= 0 and right <= len(nums) - 1 and nums[right] == target:
            return right

        return -1

    def find_min_index(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = left - (left - right) // 2
            midVal = nums[mid]
            rightVal = nums[right]
            if midVal < rightVal:
                right = mid
            elif midVal > rightVal:
                left = mid
            else:
                pass  # assumed no dup

        if nums[left] < nums[right]:
            return left

        if nums[left] > nums[right]:
            return right

        return -1

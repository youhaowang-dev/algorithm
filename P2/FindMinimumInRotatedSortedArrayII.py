# Array, Binary Search
# Google 3 Microsoft 2 Amazon 2 Facebook 4 Wish 3 Uber 2
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,4,4,5,6,7] might become:

# [4,5,6,7,0,1,4] if it was rotated 4 times.
# [0,1,4,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.

# You must decrease the overall operation steps as much as possible.

# Example 1:
# Input: nums = [1,3,5]
# Output: 1
# Example 2:
# Input: nums = [2,2,2,0,1]
# Output: 0

# Constraints:

# nums is sorted and rotated between 1 and n times.

# Follow up: This problem is similar to Find Minimum in Rotated Sorted Array, but nums may contain duplicates. Would this affect the runtime complexity? How and why?
from ast import List


class FindMinimumInRotatedSortedArrayII:

    # O(n) because of duplicates if no duplicates O(logn)
    def findMin(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return nums[0]

        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            midVal = nums[mid]
            rightVal = nums[right]
            if midVal > rightVal:
                left = mid
            if midVal < rightVal:
                right = mid
            if midVal == rightVal:
                # cannot // 2 for duplicated length is unknown
                right -= 1

        return min(nums[left], nums[right])

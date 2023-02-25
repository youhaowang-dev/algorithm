# Array, Binary Search
# Amazon 5 Bloomberg 4 Uber 3 Adobe 3 Apple 2 Facebook 2 Google 8 Yahoo 2
# https://leetcode.com/problems/peak-index-in-a-mountain-array/description/

# An array arr a mountain if the following properties hold:

# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given a mountain array arr, return the index i such that arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

# You must solve it in O(log(arr.length)) time complexity.

# Example 1:

# Input: arr = [0,1,0]
# Output: 1
# Example 2:

# Input: arr = [0,2,1,0]
# Output: 1
# Example 3:

# Input: arr = [0,10,5,2]
# Output: 1


from typing import List

# brute force: The mountain increases until it doesn't. The point at which it stops increasing is the peak.
class PeakIndexinaMountainArray:
    def peakIndexInMountainArray(self, nums: List[int]) -> int:
        for i in range(0, len(nums)):
            if nums[i] > nums[i + 1]:
                return i


# binary search
class PeakIndexinaMountainArray2:
    def peakIndexInMountainArray(self, nums: List[int]) -> int:
        if not nums:
            return -1

        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid
            else:
                right = mid

        if nums[left] > nums[right]:
            return left
        if nums[left] < nums[right]:
            return right

        return -1

# Array, Two Pointers, Dynamic Programming, Enumeration
# Bloomberg 3 Google 3 Microsoft 3 Adobe 2 Amazon 2 Yahoo 2
# https://leetcode.com/problems/longest-mountain-in-array/

# You may recall that an array arr is a mountain array if and only if:
# arr.length >= 3
# There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given an integer array arr, return the length of the longest subarray, which is a mountain. Return 0 if there is no mountain subarray.

# Example 1:
# Input: arr = [2,1,4,7,3,2,5]
# Output: 5
# Explanation: The largest mountain is [1,4,7,3,2] which has length 5.

# Example 2:
# Input: arr = [2,2,2]
# Output: 0
# Explanation: There is no mountain.

from typing import List

# 3 passes: first pass count uphill length, second pass count downhill length, final
# input:    [1, 2, 3, 2, 1]
# uphill:   [0, 1, 2, 0, 0]
# downhill: [0, 0, 2, 1, 0]
# max length = 2+2+1
class LongestMountaininArray:
    def longestMountain(self, heights: List[int]) -> int:
        length = len(heights)

        uphill_lengths = [0] * length
        for i in range(1, length):
            if heights[i] > heights[i - 1]:
                uphill_lengths[i] = uphill_lengths[i - 1] + 1

        downhill_lengths = [0] * length
        for i in reversed(range(0, length - 1)):
            if heights[i] > heights[i + 1]:
                downhill_lengths[i] = downhill_lengths[i + 1] + 1

        max_mountain_length = 0
        index = 0
        while index < length:
            mountain_length = self.get_mountain_length(
                index, uphill_lengths, downhill_lengths
            )
            max_mountain_length = max(max_mountain_length, mountain_length)
            index += 1

        return max_mountain_length

    def get_mountain_length(self, index, uphill_lengths, downhill_lengths) -> int:
        mountain_length = 0
        uphill_length = uphill_lengths[index]
        downhill_length = downhill_lengths[index]
        if uphill_length and downhill_length:
            mountain_length = 1 + uphill_length + downhill_length

        return mountain_length


# Can you solve this problem with only one pass?
# Can you solve this problem in O(1) space?
class LongestMountaininArray1:
    def longestMountain(self, heights: List[int]) -> int:
        max_mountain_length = 0
        length = len(heights)

        i = 1
        while i < length:
            while i < length and heights[i - 1] == heights[i]:
                i += 1

            uphill_length = 0
            while i < length and heights[i - 1] < heights[i]:
                uphill_length += 1
                i += 1

            downhill_length = 0
            while i < length and heights[i - 1] > heights[i]:
                downhill_length += 1
                i += 1

            if uphill_length and downhill_length:
                max_mountain_length = max(
                    max_mountain_length, uphill_length + downhill_length + 1
                )

        return max_mountain_length

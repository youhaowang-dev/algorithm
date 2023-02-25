# https://www.lintcode.com/problem/143/description
# Given an array of n objects with k different colors (numbered from 1 to k),
# sort them so that objects of the same color are adjacent, with the colors in the order 1, 2, ... k.

# Example1
# Input:
# [3,2,2,1,4]
# 4
# Output:
# [1,2,2,3,4]

# Example2
# Input:
# [2,1,1,2,2]
# 2
# Output:
# [1,1,2,2,2]

# Challenge
# You can directly use The counting sorting algorithm scan twice, but it will cost O(k) extra memory.
# Now can you do it in use O(logk) extra memory?
from typing import List


class SortColorsII:

    # brute force: counting sort

    def sort_colors2(self, colors: List[int], k: int):
        if not colors:
            return
        if len(colors) < 2:
            return

        self.sort(colors, 0, len(colors) - 1, 1, k)

    def sort(self, colors, start, end, colorFrom, colorTo) -> None:
        if start >= end or colorFrom == colorTo:
            return

        left = start
        right = end
        colorMid = (colorFrom + colorTo) / 2

        while left <= right:
            while left <= right and colors[left] <= colorMid:
                left += 1

            while left <= right and colors[right] > colorMid:
                right -= 1

            if left <= right:
                leftCopy = colors[left]
                colors[left] = colors[right]
                colors[right] = leftCopy

        self.sort(colors, start, right, colorFrom, colorMid)
        self.sort(colors, left, end, colorMid + 1, colorTo)

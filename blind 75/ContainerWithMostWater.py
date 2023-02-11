# Array, Two Pointers, Greedy
# Amazon 16 Adobe 8 Apple 8 Bloomberg 5 Google 3 Uber 2 Microsoft 2 Facebook 2 TikTok 2 Goldman Sachs 3 Qualtrics 3 ByteDance 2 Samsung 2 Walmart Global Tech 2 VMware 2 Oracle 2 Intel 2 Intuit 2 Cisco 2 Tesla 2 DE Shaw 2 JPMorgan 2 Swiggy 4 Zoho 2 tcs 2 C3 IoT 2 Arcesium 2 Wix
# https://leetcode.com/problems/container-with-most-water/

# You are given an integer array height of length n. There are n vertical lines drawn such that the
# two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
# In this case, the max area of water (blue section) the container can contain is 49.

# Example 2:
# Input: height = [1,1]
# Output: 1

# brute force: try all pairs, n^2
class ContainerWithMostWater:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        length = len(height)
        for left in range(length):
            for right in range(left + 1, length):
                width = right - left
                min_height = min(height[left], height[right])
                max_area = max(max_area, min_height * width)

        return max_area


# area is bound by smaller height, move smaller height and calculate the area
# two pointers: left and right, move smaller height towards mid while calculating area
class ContainerWithMostWater2:
    def maxArea(self, height: List[int]) -> int:
        if not height:
            return 0

        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            width = right - left
            min_height = min(height[left], height[right])
            max_area = max(max_area, width * min_height)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

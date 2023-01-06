# Array, Binary Search
# Facebook 17 Google 5 Uber 5 Amazon 4 Bloomberg 2 Apple 2 Microsoft 2 Adobe 2 Roblox 4 Snapchat 4 HRT 3 Bloomberg 2 TikTok 2 Walmart Global Tech 3 VMware 3 Paypal 3 Yahoo 2 IXL 2 Goldman Sachs 2
# https://leetcode.com/problems/find-peak-element/
# A peak element is an element that is strictly greater than its neighbors.

# Given a 0-indexed integer array nums, find a peak element, and return its index.
# If the array contains multiple peaks, return the index to any of the peaks.

# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always
# considered to be strictly greater than a neighbor that is outside the array.

# You must write an algorithm that runs in O(log n) time.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.

# Example 2:
# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.

from ast import List


class FindPeakElement:

    # based on the assumption(-1 and len are max int), peak always exists
    # so binary search by dropping the increasing side or decreasing side
    # increase: mid_val < mid_right_val, drop left side
    # decrease: mid_val > mid_right_val, drop right side
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            mid_val = nums[mid]
            mid_right_val = nums[mid + 1]
            if mid_val > mid_right_val:
                # [mid, mid + 1] decreases, so peak is on the left side, drop [mid, right]
                right = mid

            if mid_val < mid_right_val:
                # [mid, mid + 1] increases, so peak is on the right side, drop [left, mid]
                left = mid

            if mid_val == mid_right_val:
                # either left or right is fine
                right = mid

        # either left or right is the peak, return the index of max val(peak)
        if nums[left] < nums[right]:
            return right

        return left

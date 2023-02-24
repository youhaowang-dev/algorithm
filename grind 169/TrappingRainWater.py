# Array, Two Pointers, Dynamic Programming, Stack, Monotonic Stack
# Amazon 42 Microsoft 15 Bloomberg 12 Google 9 Apple 9 Goldman Sachs 7 Adobe 5 Uber 3 Epam Systems 3
# Salesforce 2 MakeMyTrip 2 Facebook 20 Qualtrics 4 Oracle 4 Intel 3 Citadel 3 Paypal 3 Tesla 3 Intuit 2
# Yandex 2 Yahoo 2 ServiceNow 2 Rubrik 2 Sapient 2 C3 IoT 6 Snapchat 5 VMware 4 Lyft 3 Grab 3 Visa 3 Swiggy
# 3 National Instruments 3 Zoho 2 eBay 2 Coupang 2 Flipkart 2 Expedia 2 Twitch 2 Morgan Stanley 2 DE Shaw 2
# PayTM 2 Airbnb Zenefits Twitter Wix
# https://leetcode.com/problems/trapping-rain-water/

# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it can trap after raining.

# Example 1:
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
# In this case, 6 units of rain water (blue section) are being trapped.

# Example 2:
# Input: height = [4,2,0,3,2,5]
# Output: 9

# total = sum(min(i max left height, i max right height) - i height), ignore 0
# height                0, 1, 0, 3, 0, 2, 1
# left max              0, 0, 1, 1, 3, 3, 3
# right max             3, 3, 3, 2, 2, 1, 0
# min left and right    0, 0, 1, 1, 2, 1, 0
# min - height          0,-1, 1,-2, 2,-1,-1
# positive sum = 1+2 = 3
class TrappingRainWater:
    def trap(self, heights: List[int]) -> int:
        if not heights:
            return 0
        length = len(heights)

        left_maxes = [0 for _ in range(length)]
        current_left_max = 0
        for i in range(length):
            left_maxes[i] = current_left_max
            current_left_max = max(current_left_max, heights[i])

        right_maxes = [0 for _ in range(length)]
        current_right_max = 0
        for i in range(length - 1, -1, -1):
            right_maxes[i] = current_right_max
            current_right_max = max(current_right_max, heights[i])

        total = 0
        for height, left_max, right_max in zip(heights, left_maxes, right_maxes):
            min_height = min(left_max, right_max)
            water = max(0, min_height - height)
            total += water

        return total


# time : O(n) space : O(1)
# because we only need the min of max_left and max_right
# we can use two pointers to track them
# by only moving the pointer with smaller max, we can still get the min of max_left and max_right
class TrappingRainWater2:
    def trap(self, heights: List[int]) -> int:
        if not heights:
            return 0

        left = 0
        right = len(heights) - 1
        left_max = heights[left]  # NOTE: not 0
        right_max = heights[right]  # NOTE: not 0
        total = 0
        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, heights[left])
                total += max(0, left_max - heights[left])
            else:
                right -= 1
                right_max = max(right_max, heights[right])
                total += max(0, right_max - heights[right])

        return total

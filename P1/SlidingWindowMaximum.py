# Array, Queue, Sliding Window, Heap (Priority Queue), Monotonic Queue
# Amazon 31 Google 6 Apple 4 DoorDash 4 Citadel 3 Uber 2 Facebook 2 HRT 2 Microsoft 9 Adobe 5 ByteDance 5
# Salesforce 5 Bloomberg 4 VMware 3 Twitter 3 Twilio 3 Booking.com 3 TikTok 3 Coinbase 3 Akuna Capital 2
# DE Shaw 2 Cruise Automation 2 Goldman Sachs 9 Rubrik 4 Walmart Global Tech 3 Yahoo 3 Oracle 2 Infosys 2
# Atlassian 2 TuSimple 2 Quora 2 Capgemini 2 Zenefits

# https://leetcode.com/problems/sliding-window-maximum/

# You are given an array of integers nums, there is a sliding window of size k which is moving from the very
# left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.


# Example 1:

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]

from collections import deque
from typing import List

# brute force: get max for all windows
class SlidingWindowMaximum:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_of_windows = list()

        if not nums or k == 0:
            return max_of_windows

        for i in range(0, len(nums) - k + 1):
            window = nums[i : i + k]
            max_of_windows.append(max(window))

        return max_of_windows


# build max queue
class SlidingWindowMaximum1:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window_maxes = list()
        if not nums or k == 0:
            return window_maxes

        max_queue = MaxQueue()
        for i in range(k):
            max_queue.enqueue(nums[i])

        window_maxes.append(max_queue.max())

        for i in range(k, len(nums)):
            max_queue.dequeue()
            max_queue.enqueue(nums[i])
            window_maxes.append(max_queue.max())

        return window_maxes


class MaxQueue:
    def __init__(self):
        self.queue = deque()
        self.maxes = deque()

    def enqueue(self, val: int) -> None:
        self.queue.append(val)

        #  remove tail if less than val to ensure monotone of the queue
        while self.maxes and self.maxes[-1] < val:
            self.maxes.pop()

        self.maxes.append(val)

    def dequeue(self) -> int:
        result = self.queue.popleft()

        if result == self.maxes[0]:
            self.maxes.popleft()

        return result

    def max(self) -> int:
        # max element appears at the head of the queue
        return self.maxes[0]

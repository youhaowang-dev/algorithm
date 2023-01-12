# Two Pointers, Design, Sorting, Heap (Priority Queue), Data Stream
# Amazon 22 Google 7 Apple 5 Bloomberg 4 Microsoft 3 IXL 3 ServiceNow 3 Uber 2 Intuit 2 Facebook 8 Indeed 3
# LinkedIn 3 Spotify 2 Walmart Global Tech 2 VMware 2 Citadel 2 Nvidia 2 Paypal 2 Zoom 2 ByteDance 12 Twitter 7
# Goldman Sachs 6 Adobe 6 eBay 4 Airbnb 3 Oracle 3 Salesforce 3 Expedia 2 Akuna Capital 2 Twilio 2 DoorDash 2 TikTok 2
# https://leetcode.com/problems/find-median-from-data-stream/
# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

# For example, for arr = [2,3,4], the median is 3.
# For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# Implement the MedianFinder class:

# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

# Example 1:
# Input
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# Output
# [null, null, null, 1.5, null, 2.0]

# Explanation
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0

# Follow up:

# If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
# If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?

# brute force: insert in list, when getting median, sort the list and return

# min heap stores bigger numbers, max heap stores smaller numbers
# balancing the two heaps,
from heapq import heappush, heappop


class MedianFinder:
    def __init__(self):
        self.smaller = []  # max heap
        self.bigger = []  # min heap

    # balance the size, small == big or small + 1 = big
    def addNum(self, num: int) -> None:
        if len(self.smaller) == len(self.bigger):
            self.smaller_push(num)
            larger_val = self.smaller_pop()
            self.bigger_push(larger_val)
        else:
            self.bigger_push(num)
            smaller_val = self.bigger_pop()
            self.smaller_push(smaller_val)

    def findMedian(self) -> float:
        if len(self.smaller) == len(self.bigger):
            return float(self.bigger_peek() + self.smaller_peek()) / 2.0
        else:
            return float(self.bigger_peek())

    def bigger_push(self, val: int) -> None:
        heappush(self.bigger, val)

    def bigger_pop(self) -> int:
        return heappop(self.bigger)

    def bigger_peek(self) -> int:
        return self.bigger[0]

    def smaller_push(self, val: int) -> None:
        heappush(self.smaller, -val)

    def smaller_pop(self) -> int:
        return -heappop(self.smaller)

    def smaller_peek(self) -> int:
        return -self.smaller[0]

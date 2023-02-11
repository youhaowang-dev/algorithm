# Two Pointers, Design, Sorting, Heap (Priority Queue), Data Stream
# Amazon 22 Google 7 Apple 5 Bloomberg 4 Microsoft 3 IXL 3 ServiceNow 3 Uber 2 Intuit 2 Facebook 8 Indeed 3
# LinkedIn 3 Spotify 2 Walmart Global Tech 2 VMware 2 Citadel 2 Nvidia 2 Paypal 2 Zoom 2 ByteDance 12 Twitter 7
# Goldman Sachs 6 Adobe 6 eBay 4 Airbnb 3 Oracle 3 Salesforce 3 Expedia 2 Akuna Capital 2 Twilio 2 DoorDash 2 TikTok 2
# https://leetcode.com/problems/find-median-from-data-stream/
# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value,
# and the median is the mean of the two middle values.

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


# brute force: insert in list, when getting median, sort the list and return

# Follow up:
# If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
# We can maintain an integer array of length 100 to store the count of each number along with a total count.
# Then, we can iterate over the array to find the middle value to get our median.
# Time and space complexity would be O(100) = O(1).
# If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
# we just keep a count of how many numbers are above 100 and how many numbers are below 0, since these numbers
# could never get to be the median and are therefore not important to keep
class MedianFinder:  # two heaps
    def __init__(self):
        # smaller == bigger or smaller == bigger + 1
        self.smaller_half = list()
        self.bigger_half = list()

    def addNum(self, num: int) -> None:
        if len(self.smaller_half) == len(self.bigger_half):
            # add to smaller but num could belong to bigger
            smaller_from_bigger_half = heapq.heappushpop(self.bigger_half, num)
            heapq.heappush(self.smaller_half, -smaller_from_bigger_half)
        else:
            # add to bigger but num could belong to smaller
            bigger_from_smaller_half = heapq.heappushpop(
                self.smaller_half, -num)
            heapq.heappush(self.bigger_half, -bigger_from_smaller_half)

    def findMedian(self) -> float:
        num_count = len(self.smaller_half) + len(self.bigger_half)
        if num_count % 2 == 0:
            return (-self.smaller_half[0] + self.bigger_half[0]) / 2
        else:
            return -self.smaller_half[0]

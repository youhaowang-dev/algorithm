# array, divide and conquer, sorting, heap, priority queue, quickselect
# Facebook 28 Amazon 17 Spotify 11 LinkedIn 8 Microsoft 5 Adobe 5 Apple 4 Bloomberg 3 Google 2 Walmart Global Tech 2 Intuit 2
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/

# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# You must solve it in O(n) time complexity.

# examples:
# nums = [3,2,1,5,6,4], k = 2, output = 5
# nums = [3,2,3,1,2,4,5,5,6], k = 4, output = 4


# brute force time O(nlogn): sort the input then return nums[length - k]

# min heap time O(nlogk): maintain a min heap of size k, push all elements, the peek will be the kth largest

from heapq import heappop, heappush
from typing import List


class KthLargestElementInAnArray:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = MinHeap()
        for num in nums:
            min_heap.push(num)
            # if len(min_heap) > k: # TypeError: object of type 'MinHeap' has no len()
            if min_heap.size() > k:
                min_heap.pop()

        return min_heap.peek()


class MinHeap:
    def __init__(self):
        self.min_heap = []

    def push(self, val: int) -> None:
        heappush(self.min_heap, val)

    def pop(self) -> int:
        return heappop(self.min_heap)

    def peek(self) -> int:
        return self.min_heap[0]

    def size(self) -> int:
        return len(self.min_heap)


# Quickselect is a textbook algorthm typically used to solve the problems "find kth something":
# kth smallest, kth largest, kth most frequent, kth less frequent, etc.
# Like quicksort, quickselect was developed by Tony Hoare, and also known as Hoare's selection algorithm.

# quick select to sort the half containing target
# time: O(n) where partition costs n + n/2 + n/4 + ... + = 2n
# The worst case is that partitioning always results in very skewed partition sizes.
# Consider what would happen if the first partitioning only removed one item. And the second only removed one, etc.
# The result would be: N + (N-1) + (N-2) ... Which is (n^2 + n)/2), or O(n^2).
class KthLargestElementInAnArray2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target_index = len(nums) - k
        start = 0
        end = len(nums) - 1

        return self.partition(nums, target_index, start, end)

    def partition(
        self, nums: List[int], target_index: int, start: int, end: int
    ) -> int:
        if start >= end:
            # partition containing the target has been sorted
            return nums[target_index]

        left = start
        right = end
        mid_val = nums[(start + end) // 2]
        while left <= right:
            while left <= right and nums[left] < mid_val:
                left += 1

            while left <= right and nums[right] > mid_val:
                right -= 1

            if left <= right:
                # self.swap(nums, left, right)
                (nums[left], nums[right]) = (nums[right], nums[left])
                left += 1
                right -= 1

        if target_index <= right:
            # sort next partition
            return self.partition(nums, target_index, start, right)
        else:
            # sort next partition
            return self.partition(nums, target_index, left, end)

    # def swap(self, nums, left, right):
    #     leftCopy = nums[left]
    #     nums[left] = nums[right]
    #     nums[right] = leftCopy

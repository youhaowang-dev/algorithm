# Array, Divide and Conquer, Sorting, Heap (Priority Queue), Merge Sort, Bucket Sort, Radix Sort, Counting Sort
# Microsoft 4 Apple 2 Amazon 2 Google 2 Adobe 3 Bloomberg 3 Uber 2 Yahoo 3 Intel 2 Infosys 2
# https://leetcode.com/problems/sort-an-array/
# Given an array of integers nums, sort the array in ascending order and return it.

# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity
# and with the smallest space complexity possible.

# Example 1:
# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3),
# while the positions of other numbers are changed (for example, 1 and 5).

# Example 2:
# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
# Explanation: Note that the values of nums are not necessairly unique.


from typing import List

# merge sort time O(nlogn) stable space O(n)
class SortanArray:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.merge_sort(nums)

    def merge_sort(self, nums):
        nums_len = len(nums)
        if nums_len == 1:
            return nums

        partition_index = nums_len // 2

        left_half = nums[:partition_index]
        sorted_left_half = self.merge_sort(left_half)

        right_half = nums[partition_index:]
        sorted_right_half = self.merge_sort(right_half)

        return self.merge_sorted_arrays(sorted_left_half, sorted_right_half)

    def merge_sorted_arrays(self, left_half, right_half):
        merged = []
        left, right = 0, 0
        while left < len(left_half) and right < len(right_half):
            if left_half[left] <= right_half[right]:
                merged.append(left_half[left])
                left += 1
            else:
                merged.append(right_half[right])
                right += 1

        if left < len(left_half):
            return merged + left_half[left:]
        if right < len(right_half):
            return merged + right_half[right:]

        return merged


# quick sort time O(nlogn) space O(logn)
# worst time is O(n^2) when the picked pivot is always an extreme (smallest or largest) element
class SortanArray1:
    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        self.quick_sort(nums, 0, len(nums) - 1)

        return nums

    def quick_sort(self, nums: List[int], start: int, end: int) -> None:
        if start >= end:
            return

        left = start
        right = end
        pivot_index = (start + end) // 2
        pivot = nums[pivot_index]
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                self.swap(nums, left, right)
                left += 1
                right -= 1
        self.quick_sort(nums, start, right)
        self.quick_sort(nums, left, end)

    def swap(self, nums: List[int], index1: int, index2: int) -> None:
        (nums[index1], nums[index2]) = (nums[index2], nums[index1])
        # val1_copy = nums[index1]
        # nums[index1] = nums[index2]
        # nums[index2] = val1_copy

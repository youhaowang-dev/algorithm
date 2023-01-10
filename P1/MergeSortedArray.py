# Array, Two Pointers, Sorting
# Facebook 9 Amazon 7 Google 5 Microsoft 4 Oracle 3 Bloomberg 2 Adobe 2 Apple 2 Indeed 2 LinkedIn 2 Yahoo 2 Reddit 2
# https://leetcode.com/problems/merge-sorted-array/description/

# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
# representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
# To accommodate self, nums1 has a length of m + n, where the first m elements denote the elements that should be
# merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

# Example 1:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

# Example 2:
# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].

# Example 3:
# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.


from typing import List


class MergeSortedArray:

    # merge backward to avoid O(n) inserts
    # insert bigger number while moving pointers
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # pointers
        nums1_last = m - 1
        nums_Last = n - 1
        insert_index = len(nums1) - 1
        while nums1_last >= 0 and nums_Last >= 0:
            if nums1[nums1_last] > nums2[nums_Last]:
                nums1[insert_index] = nums1[nums1_last]
                nums1_last -= 1
                insert_index -= 1
            else:
                nums1[insert_index] = nums2[nums_Last]
                nums_Last -= 1
                insert_index -= 1

        while nums1_last >= 0:
            nums1[insert_index] = nums1[nums1_last]
            nums1_last -= 1
            insert_index -= 1

        while nums_Last >= 0:
            nums1[insert_index] = nums2[nums_Last]
            nums_Last -= 1
            insert_index -= 1


class MergeSortedArray2:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        iterator = SortedArraysIterator(nums1, m, nums2, n)
        insertPosition = len(nums1) - 1

        while insertPosition >= 0 and iterator.hasNextMax():
            nums1[insertPosition] = iterator.getNextMax()
            insertPosition -= 1


class SortedArraysIterator:
    def __init__(self, arr1, length1, arr2, length2):
        self.arr1 = arr1
        self.last1 = length1 - 1
        self.arr2 = arr2
        self.last2 = length2 - 1

    def getNextMax(self) -> int:
        if not self.hasNextMax():
            return float("inf")

        if self.list1HasNext() and self.list2HasNext():
            if self.arr1[self.last1] < self.arr2[self.last2]:
                num = self.arr2[self.last2]
                self.last2 -= 1

                return num
            else:
                num = self.arr1[self.last1]
                self.last1 -= 1

                return num

        if self.list1HasNext():
            num = self.arr1[self.last1]
            self.last1 -= 1
            return num

        if self.list2HasNext():
            num = self.arr2[self.last2]
            self.last2 -= 1
            return num

        return float("inf")

    def hasNextMax(self) -> bool:
        return self.list1HasNext() or self.list2HasNext()

    def list1HasNext(self) -> bool:
        return self.last1 >= 0

    def list2HasNext(self) -> bool:
        return self.last2 >= 0

# Array, Binary Search, Divide and Conquer
# Amazon 33 Microsoft 13 Google 12 Bloomberg 12 Adobe 10 Apple 10 Uber 7 Goldman Sachs 4 Yahoo 4 tcs 4 Facebook 3 LinkedIn 2 Mathworks 2 TikTok 2 Zoho 2
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) // 2 = 2.5.


from ast import List


class MedianOfTwoSortedArrays(object):
    # brute force
    # merge two arrays and find the median
    # O(m+n)
    # binary search the kth largest number of 2 sorted arrays; k is 1 based index
    # find median => find median index(s) => find kth largest number for the index(s) => calculate median
    # A[1,3,5,7], B[2,4,6], target 4th largest
    # k: 4, index1: 0, pivot1: 1, index2: 0, pivot2: 1 ==> k: 2, index1: 2, index2: 0
    # k: 2, index1: 2, pivot1: 2, index2: 0, pivot2: 0 ==> k: 1, index1: 2, index2: 1
    # k: 1, return min(A[2],B[1]) = min(5,4) = 4
    # 3 cases
    #    A[k/2-1] < B[k/2-1], A[0, k/2-1] can be dropped
    #    B[k/2-1] < A[k/2-1], B[0, k/2-1] can be dropped
    #    A[k/2-1] == B[k/2-1], same as A[k/2-1] < B[k/2-1]
    # special cases
    #    A[k/2-1] or B[k/2-1] out of bound, get the last element; we cannot simply remove k/2
    #    index == length, search is finished, just return kth in the other array
    #    k == 1, return min(A[i], B[j])
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length1 = len(nums1)
        length2 = len(nums2)
        total_len = length1 + length2
        kth = int(total_len // 2) + 1
        if total_len % 2 == 1:
            return self.getKthElement(nums1, nums2, kth)
        else:
            left = self.getKthElement(nums1, nums2, kth - 1)
            right = self.getKthElement(nums1, nums2, kth)

            return (left + right) / 2

    def getKthElement(self, nums1, nums2, k):
        length1 = len(nums1)
        length2 = len(nums2)
        index1 = 0
        index2 = 0
        while k != 1:
            # all nums1 are dropped
            if index1 == length1:
                return nums2[index2 + k - 1]
            # all nums2 are dropped
            if index2 == length2:
                return nums1[index1 + k - 1]
            # get the next index if drop k/2 elements
            half_k = k // 2
            pivot1 = min(index1 + half_k, length1) - 1
            pivot2 = min(index2 + half_k, length2) - 1
            if nums1[pivot1] <= nums2[pivot2]:
                # [index1, pivot1] has no target; continue in [pivot1+1, end]
                droppedCount = pivot1 - index1 + 1
                k = k - droppedCount
                index1 = pivot1 + 1
            else:
                # [index2, pivot2] has no target; continue in [pivot2+1, end]
                droppedCount = pivot2 - index2 + 1
                k = k - droppedCount
                index2 = pivot2 + 1
        # k == 1
        val1 = 0
        if index1 < 0 or index1 > length1 - 1:
            val1 = float("inf")
        else:
            val1 = nums1[index1]
        val2 = 0
        if index2 < 0 or index2 > length2 - 1:
            val2 = float("inf")
        else:
            val2 = nums2[index2]
        return min(val1, val2)

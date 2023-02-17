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

class MedianOfTwoSortedArrays:
    # brute force
    # merge k + 1 elements from the list, return k or (k + k+1) // 2

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
        kth = (total_len + 1) // 2
        if total_len % 2 == 1:
            return self.get_kth(nums1, 0, nums2, 0, kth)
        else:
            return (
                self.get_kth(nums1, 0, nums2, 0, kth) +
                self.get_kth(nums1, 0, nums2, 0, kth + 1)
            ) / 2

    def get_kth(self, nums1, start1, nums2, start2, k) -> int:
        if start1 >= len(nums1):
            return nums2[start2 + k - 1]
        if start2 >= len(nums2):
            return nums1[start1 + k - 1]
        if k == 1:
            return min(nums1[start1], nums2[start2])

        drop_count = k // 2
        new_start1 = start1 + drop_count - 1
        new_start2 = start2 + drop_count - 1
        val1 = math.inf if new_start1 >= len(nums1) else nums1[new_start1]
        val2 = math.inf if new_start2 >= len(nums2) else nums2[new_start2]

        if val1 <= val2:
            return self.get_kth(nums1, new_start1 + 1, nums2, start2, k - drop_count)
        else:
            return self.get_kth(nums1, start1, nums2, new_start2 + 1, k - drop_count)

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
            return self.get_kth(nums1, 0, nums2, 0, kth)
        else:
            left = self.get_kth(nums1, 0, nums2, 0, kth - 1)
            right = self.get_kth(nums1, 0, nums2, 0, kth)

            return (left + right) / 2

    def get_kth(
        self: object,
        nums1: List[int],
        start1: int,
        nums2: List[int],
        start2: int,
        k: int,
    ) -> int:
        if start1 >= len(nums1):
            return nums2[start2 + k - 1]
        if start2 >= len(nums2):
            return nums1[start1 + k - 1]
        if k == 1:
            return min(nums1[start1], nums2[start2])

        half_k = k // 2
        a_pivot = start1 + half_k - 1
        b_pivot = start2 + half_k - 1
        aVal = float("inf") if a_pivot >= len(nums1) else nums1[a_pivot]
        bVal = float("inf") if b_pivot >= len(nums2) else nums2[b_pivot]

        if aVal <= bVal:
            return self.get_kth(nums1, a_pivot + 1, nums2, start2, k - half_k)
        else:
            return self.get_kth(nums1, start1, nums2, b_pivot + 1, k - half_k)

    def findMedianSortedArrays1(self, nums1: List[int], nums2: List[int]) -> float:
        length1 = len(nums1)
        length2 = len(nums2)
        total_len = length1 + length2
        kth = int(total_len // 2) + 1
        if total_len % 2 == 1:
            return self.get_kth1(nums1, nums2, kth)
        else:
            left = self.get_kth1(nums1, nums2, kth - 1)
            right = self.get_kth1(nums1, nums2, kth)
            return (left + right) / 2

    def get_kth1(self, nums1: List[int], nums2: List[int], k: int) -> int:
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
                dropped_count = pivot1 - index1 + 1
                k = k - dropped_count
                index1 = pivot1 + 1
            else:
                # [index2, pivot2] has no target; continue in [pivot2+1, end]
                dropped_count = pivot2 - index2 + 1
                k = k - dropped_count
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

    # binary search for a max partition(inclusive) position that spit two sides with same total count AND
    # shortArr[partition-1] < longArr[partition] && shortArr[partition] > longArr[partition-1]
    # binary search on short array
    # NOTE: result can go out of bound
    # [1,3,5][2,4,6] => expect 1 3 | 5 and 2 | 4 6 => shortPartition=2, long=3-2=1
    # [1,2][3,4,5,6] => expect 1 2 | and 3 | 4 5 6 => shortPartition=2, long=3-2=1
    # [5,6][1,2,3,4] => expect | 5 6 and 1 2 3 | 4 => shortPartition=0, long=3-0=3
    def findMedianSortedArrays(self, nums1, nums2):
        # make sure first array is shorter
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        shortLength = len(nums1)
        longLength = len(nums2)
        # make odd and even the same count
        totalLeftCount = (shortLength + longLength + 1) // 2
        shortPartition = self.partition(nums1, nums2)
        longPartition = totalLeftCount - shortPartition

        maxPartitionLeftVal = self.get_max_partition_left_val(
            nums1, nums2, shortPartition, longPartition
        )
        if (shortLength + longLength) % 2 == 1:
            return maxPartitionLeftVal

        minPartitionVal = self.get_min_partition_val(
            nums1, nums2, shortPartition, longPartition
        )

        return (maxPartitionLeftVal + minPartitionVal) * 0.5

    def partition(self, shortArr, longArr):
        left = 0
        right = len(shortArr)  # this is fine as left(-1) is needed
        # make odd and even the same count
        totalLeftCount = (len(shortArr) + len(longArr) + 1) // 2
        # binary search a max partition in short array that can make shortPartitionLeftVal <= longPartitionVal
        while left < right:
            # + 1 prevent infinite loop
            partition = (left + right + 1) // 2
            longArrPartition = totalLeftCount - partition
            if shortArr[partition - 1] > longArr[longArrPartition]:
                # partition is too big drop right part
                right = partition - 1
            else:
                # partition is okay drop the left part to make it bigger
                left = partition

        return left

    def get_max_partition_left_val(self, nums1, nums2, shortPartition, longPartition):
        shortPartitionLeftVal = (
            float("-inf") if shortPartition == 0 else nums1[shortPartition - 1]
        )
        longPartitionLeftVal = (
            float("-inf") if longPartition == 0 else nums2[longPartition - 1]
        )

        return max(shortPartitionLeftVal, longPartitionLeftVal)

    def get_min_partition_val(self, nums1, nums2, shortPartition, longPartition):
        shortPartitionVal = (
            float("inf") if shortPartition == len(nums1) else nums1[shortPartition]
        )
        longPartitionVal = (
            float("inf") if longPartition == len(nums2) else nums2[longPartition]
        )

        return min(shortPartitionVal, longPartitionVal)

# Array, Hash Table, Two Pointers, Binary Search, Sorting
# Amazon 4 Apple 8 Google 7 Facebook 7 Bloomberg 4 Adobe 3 LinkedIn 6 Microsoft 5 Yahoo 2 JPMorgan 2 Yandex 2 VMware 2 Two Sigma Wix
# https://leetcode.com/problems/intersection-of-two-arrays/

# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]

# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.

from typing import List


# brute force m*n
class IntersectionOfTwoArrays:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = set()
        for num1 in nums1:
            for num2 in nums2:
                if num1 == num2:
                    intersection.add(num1)

        return list(intersection)


# hash set
# preprocess data to sets for fast access and dedup
# if one set is much larger than the other, find the smaller size set and use it for loop
class IntersectionOfTwoArrays2:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_set = set()
        for num in nums1:
            nums1_set.add(num)

        nums2_set = set()
        for num in nums2:
            nums2_set.add(num)

        result = list()
        for num in nums1_set:
            if num in nums2_set:
                result.append(num)

        return result

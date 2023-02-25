# Array, Hash Table, Two Pointers, Binary Search, Sorting
# Amazon 3 Facebook 2 Adobe 2 Bloomberg 3 Yahoo 3 Uber 2 Microsoft 2 Google 5 LinkedIn 4 Apple 4 Yandex 4 Nutanix 2 Walmart Global Tech 2
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.

from typing import List

# brute force m*n
class IntersectionOfTwoArrays:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = list()

        if not nums1 or not nums2:
            return result

        if len(nums1) > len(nums2):
            # make nums1 the shorter one
            nums1, nums2 = nums2, nums1

        i = 0
        while i < len(nums1):
            if nums1[i] in nums2:
                result.append(nums1[i])
                nums2.remove(nums1[i])
                nums1.remove(nums1[i])
                i -= 1
            i += 1

        return result


# sort + two pointers
class IntersectionofTwoArraysII2:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = list()

        if not nums1 or not nums2:
            return result

        get_sort_key = lambda num: num
        nums1, nums2 = sorted(nums1, key=get_sort_key), sorted(nums2, key=get_sort_key)

        nums1_index, nums2_index = 0, 0
        while nums1_index < len(nums1) and nums2_index < len(nums2):
            if nums1[nums1_index] < nums2[nums2_index]:
                nums1_index += 1
            elif nums1[nums1_index] > nums2[nums2_index]:
                nums2_index += 1
            else:
                result.append(nums1[nums1_index])
                nums1_index += 1
                nums2_index += 1

        return result


# need to use a hash map to track the count for each number.
class IntersectionofTwoArraysII3:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = list()

        if not nums1 or not nums2:
            return result

        num_to_count = dict()
        for num in nums1:
            num_to_count[num] = 1 + num_to_count.get(num, 0)

        for num in nums2:
            if num in num_to_count and num_to_count[num] > 0:
                result.append(num)
                num_to_count[num] -= 1

        return result

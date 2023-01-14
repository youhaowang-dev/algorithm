# Array, Two Pointers, Sorting
# Amazon 11 Apple 4 Bloomberg 4 Facebook 3 Audible 2 Google 4 Adobe 3 Uber 3 Microsoft 3 Infosys 3 LinkedIn 2 Rubrik 2 Yahoo 4 Snapchat 4
# https://leetcode.com/problems/4sum/

# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

# Example 1:
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

# Example 2:
# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]

from copy import copy
from typing import List


class FourSum:

    # dfs n sum + two sum
    # depth first search
    # can easily convert to kth for followup
    # use long for sum if interviewer say numbers are large and can overflow
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = list()
        if not nums:
            return results
        nums.sort()
        state = list()
        self.searchSum(nums, state, target, results, 0)

        return results

    def searchSum(
        self,
        nums: List[int],
        list: List[int],
        target: int,
        results: List[List[int]],
        start: int,
    ):
        if len(list) == 4:
            if target == 0:
                results.append(copy.deepcopy(list))

            return

        for i in range(start, len(nums)):
            if i != start and nums[i] == nums[i - 1]:
                continue

            list.append(nums[i])
            self.searchSum(nums, list, target - nums[i], results, i + 1)
            list.pop()


# four pointers
class FourSum2:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = list()
        if not nums:
            return results

        nums.sort()
        length = len(nums)
        for i in range(length):
            for j in range(i + 1, length):
                self.twoSum(nums, target, nums[i], nums[j], j + 1, length - 1, results)

        return list(set(results))

    def twoSum(
        self,
        nums: List[int],
        target: int,
        num1: int,
        num2: int,
        left: int,
        right: int,
        results: List[List[int]],
    ):
        target_remain = target - num1 - num2
        while left < right:
            if nums[left] + nums[right] < target_remain:
                left += 1
            elif nums[left] + nums[right] > target_remain:
                right -= 1
            else:
                # results.append([num1, num2, nums[left], nums[right]]) TypeError: unhashable type: 'list'
                results.append((num1, num2, nums[left], nums[right]))
                left += 1
                right -= 1

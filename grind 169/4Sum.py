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


# 4 sum -> n sum -> two sum
# O(n^4)
class FourSum:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        return self.n_sum(nums, target, 4)

    def n_sum(self, nums, target, n) -> List[List[int]]:
        if n == 2:
            return self.two_sum(nums, target)

        results = list()
        prev_used_num = None
        for i in range(len(nums)-n+1):
            if nums[i] == prev_used_num:
                continue

            sum_results = self.n_sum(nums[i+1:], target-nums[i], n-1)
            for sum_result in sum_results:
                sum_result.append(nums[i])
            results.extend(sum_results)
            prev_used_num = nums[i]

        return results

    # two pointers
    def two_sum(self, nums, target) -> List[List[int]]:
        left = 0
        right = len(nums)-1
        res = list()
        while left < right:
            temp = nums[left] + nums[right]
            if temp == target:
                res.append([nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
                while left < right and nums[right] == nums[right+1]:
                    right -= 1
            elif temp < target:
                left += 1
            elif temp > target:
                right -= 1

        return res

# sort + four pointers


class FourSum2:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = list()
        if not nums:
            return results

        nums.sort()
        length = len(nums)
        for i in range(length):
            for j in range(i + 1, length):
                self.twoSum(nums, target, nums[i],
                            nums[j], j + 1, length - 1, results)

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


# dfs n sum + two sum
# depth first search
# can easily convert to kth for followup
# use long for sum if interviewer say numbers are large and can overflow
class FourSum3:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = list()
        if not nums:
            return results

        nums.sort()  # dedup
        num_list = list()
        start_index = 0
        needed_num_count = 4
        self.n_sum(nums, target, num_list, results,
                   start_index, needed_num_count)

        return results

    def n_sum(
        self,
        nums: List[int],
        target: int,
        num_list: List[int],
        results: List[List[int]],
        start_index: int,
        needed_num_count,
    ):
        if len(num_list) == needed_num_count:
            if target == 0:
                # results.append(copy.deepcopy(num_list))
                results.append(list(num_list))
            return

        for i in range(start_index, len(nums)):
            if i != start_index and nums[i] == nums[i - 1]:
                continue

            num_list.append(nums[i])
            self.n_sum(nums, target - nums[i], num_list,
                       results, i + 1, needed_num_count)
            num_list.pop()

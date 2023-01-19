# Array, Backtracking, Bit Manipulation
# Amazon 5 Google 2 Yahoo 2 Bloomberg 4 Facebook 3 Adobe 3 Apple 3 Uber 2 TikTok 2
# https://leetcode.com/problems/subsets-ii/

# Given an integer array nums that may contain duplicates, return all possible
# subsets(the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:
# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Example 2:
# Input: nums = [0]
# Output: [[],[0]]

from ast import List

# time O(n * 2^n) generate all subsets and then copy them into output list
# space O(n * 2^n) This is exactly the number of solutions for subsets multiplied by the number N of elements to keep for each subset.
# For a given number, it could be present or absent (i.e. binary choice) in a subset solution.
# As as result, for N numbers, we would have in total 2^N choices (solutions).
# print(subset_state) for [2,1,2] => [1,2,2]
# []
# [1]
# [1, 2]
# [1, 2, 2]
# [2]
# [2, 2]
class SubsetsII:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = list()
        if not nums:
            return result
        # sort is need for dedup because same number need to be ordered
        # For example input is {2,1,2}. In the backtrack we can have {2,1} and {1,2}.
        # To avoid this we sort first. Making the list {1,2,2}, so in the backtrack we can skip the second {1, 2}
        nums.sort()  # for dedup
        subset_state = list()
        start_index = 0
        self.subsetsWithDupHelper(nums, subset_state, result, start_index)

        return result

    def subsetsWithDupHelper(self, nums, subset_state, result, start_index):
        result.append(list(subset_state))
        for i in range(start_index, len(nums)):
            if i > start_index and nums[i] == nums[i - 1]:
                continue
            subset_state.append(nums[i])
            self.subsetsWithDupHelper(nums, subset_state, result, i + 1)
            subset_state.pop()

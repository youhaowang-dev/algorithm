# Array, Backtracking
# Amazon 15 Microsoft 4 Bloomberg 3 Adobe 3 Google 2 Yahoo 2 Walmart Global Tech 2 Citadel 2 Uber 2 Facebook 7
# LinkedIn 4 Apple 4 TikTok 3 Paypal 2 Goldman Sachs 2 GoDaddy 2 Nvidia 2 Visa 2 eBay 6 Oracle 4 ByteDance 4 Snapchat 2 PayTM 2
# https://leetcode.com/problems/permutations/

# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:
# Input: nums = [1]
# Output: [[1]]
from ast import List
from collections import deque

# time O(n*n!) space O(n*n!)
# we have N choices, each choice has (N - 1) choices, and so on.
# Notice that at the end when deep copying the list to the result list, it takes O(N).
# Second, the space complexity should also be N x N!
# since we have N! solutions and each of them requires N space to store elements.
class Permutations:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = list()
        if not nums:
            return result

        # permutation is ordered, so need a fast way to mark used number
        used = [False for _ in range(len(nums))]
        list_state = list()
        self.permuteHelper(nums, used, list_state, result)

        return result

    def permuteHelper(self, nums, used, list_state, result) -> None:
        if len(list_state) == len(nums):
            result.append(list(list_state))
            return

        for i in range(0, len(nums)):
            if used[i]:
                continue

            list_state.append(nums[i])
            used[i] = True
            self.permuteHelper(nums, used, list_state, result)
            list_state.pop()
            used[i] = False


# build permutation while iteratively dfs
# deque([([1, 2, 3], [])])
# deque([([2, 3], [1]), ([1, 3], [2]), ([1, 2], [3])])
# ...
# deque([([2, 3], [1]), ([1, 3], [2]), ([2], [3, 1]), ([], [3, 2, 1])])
# ...
# deque([([2, 3], [1]), ([1, 3], [2]), ([], [3, 1, 2])])
# ...
# deque([([2, 3], [1]), ([3], [2, 1]), ([], [2, 3, 1])])
# ...
# deque([([2, 3], [1]), ([], [2, 1, 3])])
# ...
# deque([([3], [1, 2]), ([], [1, 3, 2])])
# ...
class Permutations2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = list()
        if not nums:
            return result

        permutation_state = list()
        stack = deque()
        stack.append((nums, permutation_state))
        while stack:
            nums, path = stack.pop()
            if not nums:
                result.append(path)
            for i in range(len(nums)):
                new_nums = nums[:i] + nums[i + 1 :]
                stack.append((new_nums, path + [nums[i]]))

        return result

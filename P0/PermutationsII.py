# Array, Backtracking
# LinkedIn 2 Amazon 2 Microsoft 3 Google 2 Bloomberg 2 Apple 2 Facebook 3 Adobe 3 Oracle 2
# https://leetcode.com/problems/permutations-ii/description/

# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

# Example 1:
# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
# Example 2:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

from ast import List

# [2,1,1] print(permutation_state)
# []
# [1]
# [1, 1], [1, 2]
# [1, 1, 2], [1, 2, 1]
# [2]
# [2, 1]
# [2, 1, 1]
class PermutationsII:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = list()
        if not nums:
            return result

        nums.sort()  # required for dedup
        used = [False for _ in range(0, len(nums))]
        permutation_state = list()
        self.permuteUniqueHelper(nums, permutation_state, result, used)

        return result

    def permuteUniqueHelper(self, nums, permutation_state, result, used):
        if len(permutation_state) == len(nums):
            result.append(list(permutation_state))
            return

        for i in range(0, len(nums)):
            if used[i]:
                continue
            # dont skip if prev is not used yet
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue

            permutation_state.append(nums[i])
            used[i] = True
            self.permuteUniqueHelper(nums, permutation_state, result, used)
            permutation_state.pop()
            used[i] = False

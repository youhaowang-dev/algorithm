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

# time O(n * 2^n) generate all subsets and then copy them into output list
# space O(n * 2^n) This is exactly the number of solutions for subsets multiplied by the number N of elements to keep for each subset.
# For a given number, it could be present or absent (i.e. binary choice) in a subset solution.
# As as result, for N numbers, we would have in total 2^N choices (solutions).
class SubsetsII:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return list()

        num_to_count = collections.Counter(nums)
        results = list()
        result = list()
        unique_nums = list(num_to_count.keys())
        start = 0
        self.build_results(results, result, unique_nums, num_to_count, start)

        return results

    def build_results(self, results, result, nums, num_to_count, start):
        results.append(list(result))

        for i in range(start, len(nums)):
            num = nums[i]
            if num_to_count[num] == 0:
                continue

            result.append(num)
            num_to_count[num] -= 1
            self.build_results(results, result, nums, num_to_count, i)
            result.pop()
            num_to_count[num] += 1

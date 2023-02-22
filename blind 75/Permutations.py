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

# time O(n*n!) space O(n*n!)
# we have N choices, each choice has (N - 1) choices, and so on.
# Notice that at the end when deep copying the list to the result list, it takes O(N).
# Second, the space complexity should also be N x N!
# since we have N! solutions and each of them requires N space to store elements.
class Permutations:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return list()

        results = list()
        result = list()
        used = set()
        self.build_results(nums, results, result, used)

        return results

    def build_results(self, nums, results, result, used):
        if len(result) == len(nums):
            results.append(list(result))
            return

        for i, num in enumerate(nums):
            if i in used:
                continue

            result.append(num)
            used.add(i)
            self.build_results(nums, results, result, used)
            result.pop()
            used.remove(i)

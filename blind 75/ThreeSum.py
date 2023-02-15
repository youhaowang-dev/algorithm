# Array, Two Pointers, Sorting
# Amazon 26 Apple 12 Facebook 8 Adobe 8 Microsoft 7 Bloomberg 6 Uber 4 Walmart Global Tech 4 Yahoo 3
# MakeMyTrip 3 Goldman Sachs 2 Google 2 Visa 2 Cisco 2 TikTok 6 Salesforce 4 Infosys 4 Qualtrics 3 VMware 3
# Morgan Stanley 3 LinkedIn 2 ByteDance 2 Oracle 2 Tesla 2 American Express 2 Intel 2

# https://leetcode.com/problems/3sum/

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.

# sort + three pointers
class ThreeSum:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = set()
        if not nums or len(nums) < 3:
            return results

        nums.sort()  # so the sum is predictable, so pointers can move accordingly
        for i in range(len(nums)):
            # if i > 0 and nums[i] == nums[i-1]: continue
            self.build_results(nums, i, results)

        return map(list, results)

    def build_results(self, nums, start, results):
        left = start + 1
        right = len(nums) - 1
        while left < right:
            total = nums[start] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            elif total == 0:
                results.add((nums[start], nums[left], nums[right]))
                left += 1
                right -= 1
                # while left < right and nums[left] == nums[left-1]: left += 1
                # while left < right and nums[right] == nums[right+1]: right -= 1

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

# sort + two pointers, three sum => two sum
class ThreeSum:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = list()
        if not nums:
            return results

        nums.sort()
        for i in range(0, len(nums)):
            if nums[i] > 0:  # optional
                break
            if i != 0 and nums[i - 1] == nums[i]:
                continue

            self.search_sum(nums, i, results)

        return results

    def search_sum(self, nums: List[int], i: int, results: List[List[int]]) -> None:
        left = i + 1
        right = len(nums) - 1
        while left < right:
            three_sum = nums[i] + nums[left] + nums[right]
            if three_sum < 0:
                left += 1
            elif three_sum > 0:
                right -= 1
            elif three_sum == 0:  # find a result, add it, and dedup
                results.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1


# sort + hashset, three sum => two sum
class ThreeSum2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = list()
        if not nums:
            return res

        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSum(nums, i, res)
        return res

    def twoSum(self, nums: List[int], i: int, res: List[List[int]]):
        seen = set()
        first_num = nums[i]
        j = i + 1
        while j < len(nums):
            sum = first_num + nums[j]
            target = 0 - sum
            if target in seen:
                res.append([first_num, nums[j], target])
                while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                    j += 1

            seen.add(nums[j])
            j += 1

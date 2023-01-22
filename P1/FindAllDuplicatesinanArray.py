# Array, Hash Table
# Amazon 5 Microsoft 5 Adobe 5 Apple 4 Facebook 3 Google 3 Nagarro 2 Visa 2 Bloomberg 3 Oracle 2 Tencent 2 Pocket Gems
# https://leetcode.com/problems/find-all-duplicates-in-an-array/
# Given an integer array nums of length n where all the integers of nums are in the range [1, n]
# and each integer appears once or twice, return an array of all the integers that appears twice.

# You must write an algorithm that runs in O(n) time and uses only constant extra space.

# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [2,3]
# Example 2:

# Input: nums = [1,1,2]
# Output: [1]
# Example 3:

# Input: nums = [1]
# Output: []

from ast import List


# space does not include output
# Sort and Compare Adjacent Elements: time nlogn

# make num negative to mark the number as SEEN, use index converted from the number to mark it, index=abs(num)-1
# [1,2,3,2,1] => [2, 1]
# num 1 index 0 nums [-1, 2, 3, 2, 1]
# num 2 index 1 nums [-1, -2, 3, 2, 1]
# num 3 index 2 nums [-1, -2, -3, 2, 1]
# num 2 index 1 nums [-1, -2, -3, 2, 1]
# num 1 index 0 nums [-1, -2, -3, 2, 1]
class FindAllDuplicatesinanArray:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        results = list()
        if not nums:
            return results

        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                results.append(abs(num))
            else:
                nums[index] = -nums[index]

        return results

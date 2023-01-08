# Array, Two Pointers
# Facebook 10 Yandex 9 Bloomberg 5 Amazon 4 Apple 3 Google 3 Adobe 3 Microsoft 2 Oracle 2 Tesla 2 Expedia 3 Splunk 3 Uber 2 Yahoo 2 ServiceNow 2 JPMorgan 2 Samsung 2 tcs 5 VMware 4 ByteDance 4 eBay 3 SAP 3 IBM 3 Morgan Stanley 3 Cisco 3 Goldman Sachs 3 Capital One 3 TikTok 3 Walmart Global Tech 2 Salesforce 2 Zoho 2 Zillow 2 Infosys 2 BlackRock 2 Nvidia 2 Wix
# https://leetcode.com/problems/move-zeroes/

# Given an integer array nums, move all 0's to the end of it while
# maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:
# Input: nums = [0]
# Output: [0]

from typing import List


# increase 0 count along the way, swap 0 to right(i) and decrease 0 count
# O(n)
class MoveZeroes:
    ZERO = 0

    def moveZeroes(self, nums: List[int]) -> None:
        zero_count = 0
        for i in range(0, len(nums)):
            if nums[i] == self.ZERO:
                zero_count += 1

            if zero_count != self.ZERO:
                zero_index = i - zero_count
                (nums[i], nums[zero_index]) = (nums[zero_index], nums[i])

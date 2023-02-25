# Array, Hash Table, Prefix Sum
# Amazon 15 Facebook 14 Microsoft 7 Google 6 Mathworks 5 Bloomberg 4 Yandex 4 Expedia 3 TikTok 3 Apple 2 Oracle 2 Citadel 2 Infosys 2 Bolt 2 DRW 2
# https://leetcode.com/problems/subarray-sum-equals-k/

# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

# Example 1:
# Input: nums = [1,1,1], k = 2
# Output: 2

# Example 2:
# Input: nums = [1,2,3], k = 3
# Output: 2
from typing import List

# brute force: O(n^3) check all subarrays and calculate the sum and compare
# brute force: O(n^2) prefixsum + check all subarrays

# one pass O(n)
# two cases: prefixsum(0, i) == target and prefixsum(0, i) = target + subarraysum(j, i)
#    subarraysum(j, i) = prefixsum(0, i) - target
# dict to store key=prefixsum(0, i) value=sumCount
# 1. prefix sum == target => count++
# 2. subarraysum(j, i) is in dict => count += prevCount

# prefix sum
# if there exists some subarray from i to j summing to target in nums, then we know that
# prefix_sum[j] - prefix_sum[i] = target => prefix_sum[j] - target = prefix_sum[i]


class SubarraySumEqualsK:

    # [1,-1,1,-1,1], target 1 => expect 6, [1][1][1][1,-1,1][1,-1,1][1,-1,1,-1,1]
    # 1:                     prefixsum 1 == 1, count++ = 1, dict={1:1, prev_prefix_sum 0 not in dict
    # 1+(-1):                prefixsum 0 != 1, count = 1, dict={1:1,0:1, prev_prefix_sum -1 not in dict
    # 1+(-1)+1:              prefixsum 1 == 1, count++ = 2, dict={1:2,0:1, prev_prefix_sum 0 in dict, count+=1=2+1=3
    # 1+(-1)+1+(-1):         prefixsum 0 != 1, count = 3, dict={1:2,0:2, prev_prefix_sum -1 not in dict
    # 1+(-1)+1+(-1)+1:       prefixsum 1 == 1, count++ = 4, dict={1:3,0:2, prev_prefix_sum 0 in dict, count+=2=4+2=6
    def subarraySum(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0

        count = 0
        prefix_sum_to_count = dict()
        prefix_sum_to_count[0] = 1  # sum=0 has occured once
        prefix_sum = 0
        for num in nums:
            prefix_sum += num
            # prefixsum=3,target=2, target=1, if 1 exists, increase the total count
            # prefixsum=2,target=2, target=0, if 0 exists, increase the total count
            target_prefix_sum = prefix_sum - target
            if target_prefix_sum in prefix_sum_to_count:
                count += prefix_sum_to_count.get(target_prefix_sum)

            prefix_sum_to_count[prefix_sum] = 1 + \
                prefix_sum_to_count.get(prefix_sum, 0)

        return count

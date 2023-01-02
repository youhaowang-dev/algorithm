// Array, Hash Table, Prefix Sum
// Amazon 15 Facebook 14 Microsoft 7 Google 6 Mathworks 5 Bloomberg 4 Yandex 4 Expedia 3 TikTok 3 Apple 2 Oracle 2 Citadel 2 Infosys 2 Bolt 2 DRW 2
// https://leetcode.com/problems/subarray-sum-equals-k/

// Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

// A subarray is a contiguous non-empty sequence of elements within an array.

// Example 1:
// Input: nums = [1,1,1], k = 2
// Output: 2

// Example 2:
// Input: nums = [1,2,3], k = 3
// Output: 2
class SubarraySumEqualsK {

  // brute force: O(n^3) check all subarrays and calculate the sum and compare
  // brute force: O(n^2) prefixsum + check all subarrays

  // one pass O(n)
  // two cases: prefixsum(0, i) == target and prefixsum(0, i) = target + subarraysum(j, i)
  //    subarraysum(j, i) = prefixsum(0, i) - target
  // dict to store key=prefixsum(0, i) value=sumCount
  // 1. prefix sum == target => count++
  // 2. subarraysum(j, i) is in dict => count += prevCount

  // [1,-1,1,-1,1], target 1 => expect 6, [1][1][1][1,-1,1][1,-1,1][1,-1,1,-1,1]
  // count = 0, dict={}
  // 1:                     prefixsum 1 == 1, count++ = 1, dict={1:1}, subarraySum 0 not in dict
  // 1+(-1):                prefixsum 0 != 1, count = 1, dict={1:1,0:1}, subarraySum -1 not in dict
  // 1+(-1)+1:              prefixsum 1 == 1, count++ = 2, dict={1:2,0:1}, subarraySum 0 in dict, count+=1=2+1=3
  // 1+(-1)+1+(-1):         prefixsum 0 != 1, count = 3, dict={1:2,0:2}, subarraySum -1 not in dict
  // 1+(-1)+1+(-1)+1:       prefixsum 1 == 1, count++ = 4, dict={1:3,0:2}, subarraySum 0 in dict, count+=2=4+2=6

  public int subarraySum(int[] nums, int target) {
    int count = 0;
    Map<Integer, Integer> prefixSumToCount = new HashMap<>();

    int prefixSum = 0;
    for (int num : nums) {
      prefixSum += num;

      // sum(0, i)
      if (prefixSum == target) {
        count++;
      }

      // sum(?, i)
      int subarraySum = prefixSum - target;
      if (prefixSumToCount.containsKey(subarraySum)) {
        count += prefixSumToCount.get(subarraySum);
      }

      // update dict
      prefixSumToCount.putIfAbsent(prefixSum, 0);
      prefixSumToCount.put(prefixSum, 1 + prefixSumToCount.get(prefixSum));
    }

    return count;
  }
}

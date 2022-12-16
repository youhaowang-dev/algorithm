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

  // There could be two situations. In situation 1, the subarray with the target sum starts from the beginning of
  // the array. That means that the current prefix sum is equal to the target sum, and we increase the counter by 1.
  // In situation 2, the subarray with the target sum starts somewhere in the middle. That means we should
  // add to the counter the number of times we have seen the prefix sum curr_sum - target so far: count += h[curr_sum - target].
  // The logic is simple: the current prefix sum is curr_sum, and some elements before
  // the prefix sum was curr_sum - target. All the elements in between sum up to curr_sum - (curr_sum - target) = target.
  public int subarraySum(int[] nums, int target) {
    int count = 0;
    Map<Integer, Integer> prefixSumToCount = new HashMap<>();

    int prefixSum = 0;
    for (int num : nums) {
      prefixSum += num;
      // situation 1
      if (prefixSum == target) {
        count++;
      }

      int previousTargetSum = prefixSum - target;
      if (prefixSumToCount.containsKey(previousTargetSum)) {
        count += prefixSumToCount.get(previousTargetSum);
      }

      if (prefixSumToCount.containsKey(prefixSum)) {
        prefixSumToCount.put(prefixSum, prefixSumToCount.get(prefixSum) + 1);
      } else {
        prefixSumToCount.put(prefixSum, 1);
      }
    }

    return count;
  }
}

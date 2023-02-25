// Array, Binary Search, Sliding Window, Prefix Sum
// Apple 3 Citadel 3 Amazon 2 Microsoft 2 Facebook 6 Bloomberg 3 Goldman Sachs 3 Google 3 Adobe 2 Yahoo 2 Arcesium 2

// Given an array of positive integers nums and a positive integer target, return the minimal length of a
// subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

// Example 1:
// Input: target = 7, nums = [2,3,1,2,4,3]
// Output: 2
// Explanation: The subarray [4,3] has the minimal length under the problem constraint.
// Example 2:
// Input: target = 4, nums = [1,4,4]
// Output: 1
// Example 3:
// Input: target = 11, nums = [1,1,1,1,1,1,1,1]
// Output: 0

class MinimumSizeSubarraySum {

  public int minSubArrayLen(int target, int[] nums) {
    if (nums == null || nums.length == 0) {
      return 0;
    }

    int left = 0;
    int right = 0;
    int sum = 0;
    int minSubarrayLength = Integer.MAX_VALUE;
    while (right < nums.length) {
      sum = sum + nums[right];
      right++;

      while (sum >= target) {
        // right is now at the right bound + 1 position of the valid range
        int subarrayLength = right - left; // right-1 - left + 1 = right - left
        minSubarrayLength = Math.min(minSubarrayLength, subarrayLength);
        sum = sum - nums[left];
        left++;
      }
    }

    return minSubarrayLength == Integer.MAX_VALUE ? 0 : minSubarrayLength;
  }
}

// Array, Binary Search, Dynamic Programming
// Google 7 Amazon 5 TikTok 5 Adobe 3 Apple 3 Infosys 2 TuSimple 2 Microsoft 10 Facebook 4 Bloomberg 4 Oracle 4 Expedia 3 VMware 2 Visa 2 Walmart Global Tech 2 ByteDance 7 Twitter 5 ServiceNow 3 Samsung 3 Salesforce 2 Splunk 2 Paypal 2 MakeMyTrip 2 ZScaler 2 Huawei 2 Shopee 2 Deutsche Bank 2 HRT 2
// https://leetcode.com/problems/longest-increasing-subsequence/

// Given an integer array nums, return the length of the longest strictly increasing subsequence.

// Example 1:
// Input: nums = [10,9,2,5,3,7,101,18]
// Output: 4
// Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

// Example 2:
// Input: nums = [0,1,0,3,2,3]
// Output: 4

// Example 3:
// Input: nums = [7,7,7,7,7,7,7]
// Output: 1

class LongestIncreasingSubsequence {

  // dp
  // longestSubseq[i] = max(longestSubseq[0...j] + 1 if is increasing)
  // https://www.jiuzhang.com/solutions/longest-increasing-subsequence/
  public int lengthOfLIS(int[] nums) {
    if (nums == null || nums.length == 0) {
      return 0;
    }
    int length = nums.length;

    int[] longestSubseq = new int[length]; // the longest subsequence from 0 to index

    for (int i = 0; i < length; i++) {
      longestSubseq[i] = 1;
    }

    for (int index = 0; index < length; index++) {
      for (int prev = 0; prev < index; prev++) {
        boolean isIncreasing = nums[prev] < nums[index];
        if (isIncreasing) {
          longestSubseq[index] =
            Math.max(longestSubseq[index], longestSubseq[prev] + 1);
        }
      }
    }

    int longest = 0;
    for (int subseqLength : longestSubseq) {
      longest = Math.max(longest, subseqLength);
    }

    return longest;
  }

  // brute force
  // https://leetcode.com/problems/longest-increasing-subsequence/solutions/1326552/optimization-from-brute-force-to-dynamic-programming-explained/
  // If the current element is greater than the previous element, then we can either pick it or dont pick it because
  // we may get a smaller element somewhere ahead which is greater than previous and picking that would be optimal. So we try both options.
  // If the current element is smaller or equal to previous element, it can't be picked.
  // O(2^n)
  public int lengthOfLIS(int[] nums) {
    return this.getMaxLength(nums, 0, Integer.MIN_VALUE);
  }

  private int getMaxLength(int[] nums, int index, int prevPickedValue) {
    if (index >= nums.length) {
      // cant pick any more elements
      return 0;
    }
    // branch 1: skip the current element
    int skipCurrent = this.getMaxLength(nums, index + 1, prevPickedValue);
    // branch 2: pick current element if it is greater than previous picked element
    int pickCurrent = 0;
    if (nums[index] > prevPickedValue) {
      pickCurrent = 1 + this.getMaxLength(nums, index + 1, nums[index]);
    }

    return Math.max(pickCurrent, skipCurrent);
  }
}

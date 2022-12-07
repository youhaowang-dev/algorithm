// tag: array, 
// source: https://leetcode.com/problems/maximum-subarray/
// description: Given an integer array nums, find the subarray which has the largest sum and return its sum.
// example: maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) => 6 because [4,-1,2,1] has the largest sum = 6

class MaximumSubarray {

  // brute force
  // find all subarrays
  // find the sum
  // max the sum
  // time complexity: O(n^2) all subarrays * O(n) subarray sum = O(n^3)
  // space complexity: O(1) for no extra space usage
  private int maxSubArray(int[] nums) {
    int maxSubarraySum = Integer.MIN_VALUE;
    if (nums.length == 0) {
      return maxSubarraySum;
    }

    for (int subarray_left = 0; subarray_left < nums.length; subarray_left++) {
      for (int subarray_right = subarray_left; subarray_right < nums.length; subarray_right++) {
        int subarraySum = this.getSubArraySum(subarray_left, subarray_right, nums);
        maxSubarraySum = Math.max(maxSubarraySum, subarraySum);
      }
    }

    return maxSubarraySum;
  }

  private int getSubArraySum(int subarray_left, int subarray_right, int[] nums) {
    int sum = 0;
    for (int index = subarray_left; index < subarray_right; index++) {
      sum += nums[index];
    }

    return sum;
  }

  // record all the max sums for each index
  // only add the sum if the prev sum is positive
  // time complexity: O(n) for one pass
  // space complexity: O(n) for max sum array
  private int maxSubArrayV2(int[] nums) {
    // the smallest sum is 0 because subarray can be empty
    int maxSubarraySum = 0;
    if (nums.length == 0) {
      return maxSubarraySum;
    }

    int[] maxSums = new int[nums.length];
    maxSums[0] = nums[0]; // init

    for (int index = 1; index < nums.length; index++) {
      if (maxSums[index - 1] > 0) {
        // prev sum is positive, so it can increase the subarray sum
        maxSums[index] = nums[index] + maxSums[index - 1];
      } else {
        // prev sum is negative, no need to add it
        maxSums[index] = nums[index];
      }
      maxSubarraySum = Math.max(maxSubarraySum, maxSums[index]);
    }

    return maxSubarraySum;
  }

  public static void main(String[] args) {
    MaximumSubarray maxSubArray = new MaximumSubarray();
    int[] nums = new int[] {-2,1,-3,4,-1,2,1,-5,4};

    int bruteForceResult = maxSubArray.maxSubArray(nums);
    System.out.println("bruteForceResult: " + bruteForceResult);

    int maxSumArrayResult = maxSubArray.maxSubArrayV2(nums);
    System.out.println("maxSumArrayResult: " + maxSumArrayResult);
  }
}
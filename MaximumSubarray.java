// tag: array, 
// source: https://leetcode.com/problems/maximum-subarray/
// description: Given an integer array nums, find the subarray which has the largest sum and return its sum.
// example: maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) => 6 because [4,-1,2,1] has the largest sum = 6

class MaximumSubarray {

  // brute force
  // find all subarrays
  // find the sum
  // max the sum
  private int maxSubArray(int[] nums) {
    int maxSubarraySum = Integer.MIN_VALUE;
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

  public static void main(String[] args) {
    MaximumSubarray maxSubArray = new MaximumSubarray();
    int[] nums = new int[] {-2,1,-3,4,-1,2,1,-5,4};
    int bruteForceResult = maxSubArray.maxSubArray(nums);
    System.out.println("bruteForceResult: " + bruteForceResult);
  }
}
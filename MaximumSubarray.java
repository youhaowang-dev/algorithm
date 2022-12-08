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
  public int maxSubArray(int[] nums) {
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

  // brute force with prefix sum
  // time complexity: O(n) prefix sum array building + O(n^2) all subarrays = O(n^2)
  // space complexity: O(n) for prefix sum array
  public int maxSubArrayV3(int[] nums) {
    int maxSubArraySum = Integer.MIN_VALUE;
    if (nums.length == 0) {
      return maxSubArraySum;
    }

    int[] prefixSum = this.getPrefixSum(nums);

    for (int subarray_left = 0; subarray_left < nums.length; subarray_left++) {
      for (int subarray_right = subarray_left; subarray_right < nums.length; subarray_right++) {
        // [1,2,3] => [0,1,3,6]
        // left 0, right 1, expect 3, so 3 - 0, index 2 - index 0
        int subArraySum = prefixSum[subarray_right + 1] - prefixSum[subarray_left];
        maxSubArraySum = Math.max(maxSubArraySum, subArraySum);
      }
    }

    return maxSubArraySum;
  }

  // [1,2,3] => [0,1,3,6]
  private int[] getPrefixSum(int[] nums) {
    int[] prefixSum = new int[nums.length + 1];
    prefixSum[0] = 0;

    for (int index = 1; index < prefixSum.length; index++) {
      prefixSum[index] = prefixSum[index - 1] + nums[index - 1];
    }

    return prefixSum;
  }

  private int getSubArraySum(int subarray_left, int subarray_right, int[] nums) {
    int sum = 0;
    for (int index = subarray_left; index < subarray_right + 1; index++) {
      sum += nums[index];
    }

    return sum;
  }

  // record all the max sums for each index
  // only add the sum if the prev sum is positive
  // time complexity: O(n) for one pass
  // space complexity: O(n) for max sum array
  public int maxSubArrayV2(int[] nums) {
    if (nums.length == 0) {
      return Integer.MIN_VALUE;
    }

    int maxSubarraySum = nums[0];
    int[] maxSums = new int[nums.length];
    maxSums[0] = maxSubarraySum;

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

  public static void main(String[] args) throws Exception {
    MaximumSubarray maxSubArray = new MaximumSubarray();
    int[][] testCases = new int[][] {
      new int[] {-2,1,-3,4,-1,2,1,-5,4},
      new int[] {5},
    };
    // NOTE: the function must be public to make .getMethod work
    String[] testMethodNames = new String[] {"maxSubArray", "maxSubArrayV2", "maxSubArrayV3"};

    for (int[] nums : testCases) {
      for (String methodName : testMethodNames) {
        java.lang.reflect.Method method = maxSubArray.getClass().getMethod(methodName, int[].class);
        int maxSubArraySum = (int) method.invoke(maxSubArray, nums);
        String printContent = String.format("Function Name: %s, Input: %s, Output: %s", methodName, java.util.Arrays.toString(nums), maxSubArraySum);
        System.out.println(printContent);
      }
    }
  }
}
// tag: Array, Divide and Conquer, Dynamic Programming
// Amazon 41 Apple 10 Microsoft 9 Adobe 9 Google 8 Cisco 8 Facebook 6 LinkedIn 5 Bloomberg 5 Expedia 3 Uber 3 JPMorgan 3 Twilio 3 Oracle 2 DE Shaw
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
  public int maxSubArrayBruteForce(int[] nums) {
    int maxSubarraySum = Integer.MIN_VALUE;
    if (nums.length == 0) {
      return maxSubarraySum;
    }

    for (int subarr_left = 0; subarr_left < nums.length; subarr_left++) {
      for (
        int subarr_right = subarr_left;
        subarr_right < nums.length;
        subarr_right++
      ) {
        int subarraySum = this.getSubArraySum(subarr_left, subarr_right, nums);
        maxSubarraySum = Math.max(maxSubarraySum, subarraySum);
      }
    }

    return maxSubarraySum;
  }

  // brute force with prefix sum
  // time complexity: O(n) prefix sum array building + O(n^2) all subarrays =
  // O(n^2)
  // space complexity: O(n) for prefix sum array
  public int maxSubArrayBruteForceWithPrefixSum(int[] nums) {
    int maxSubArraySum = Integer.MIN_VALUE;
    if (nums.length == 0) {
      return maxSubArraySum;
    }

    int[] prefixSum = this.getPrefixSum(nums);

    for (int subarr_left = 0; subarr_left < nums.length; subarr_left++) {
      for (
        int subarr_right = subarr_left;
        subarr_right < nums.length;
        subarr_right++
      ) {
        // [1,2,3] => [0,1,3,6]
        // left 0, right 1, expect 3, so 3 - 0, index 2 - index 0
        int subArraySum = prefixSum[subarr_right + 1] - prefixSum[subarr_left];
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

  private int getSubArraySum(int subarr_left, int subarr_right, int[] nums) {
    int sum = 0;
    for (int index = subarr_left; index < subarr_right + 1; index++) {
      sum += nums[index];
    }

    return sum;
  }

  // "Whenever you see a question that asks for the maximum or minimum of something, consider Dynamic Programming
  // as a possibility. The difficult part of this problem is figuring out when a negative number is "worth" keeping
  //  in a subarray. We need a general way to figure out when a part of the array is worth keeping. As expected, any
  // subarray whose sum is positive is worth keeping. Let's start with an empty array, and iterate through the input,
  // adding numbers to our array as we go along. Whenever the sum of the array is negative, we know the entire array
  // is not worth keeping, so we'll reset it back to an empty array. However, we don't actually need to build the
  // subarray, we can just keep an integer variable current_subarray and add the values of each element there.
  // When it becomes negative, we reset it to 0 (an empty array)."
  // record all the max sums for each index
  // only add the sum if the prev sum is positive
  // time complexity: O(n) for one pass
  // space complexity: O(n) for max sum array, this can be improved because we only need the prev sum
  public int maxSubArrayDynamicProgramming(int[] nums) {
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
      new int[] { -2, 1, -3, 4, -1, 2, 1, -5, 4 },
      new int[] { 5 },
    };
    // NOTE: the method must be public to make .getMethod work
    String[] testMethodNames = new String[] {
      "maxSubArrayBruteForce",
      "maxSubArrayBruteForceWithPrefixSum",
      "maxSubArrayDynamicProgramming",
    };

    for (int[] nums : testCases) {
      for (String methodName : testMethodNames) {
        java.lang.reflect.Method method = maxSubArray
          .getClass()
          .getMethod(methodName, int[].class);
        int maxSubArraySum = (int) method.invoke(maxSubArray, nums);
        String printContent = String.format(
          "Method Name: %s\nInput: %s, Output: %s",
          methodName,
          java.util.Arrays.toString(nums),
          maxSubArraySum
        );
        System.out.println(printContent);
      }
    }
  }
}

// https://www.lintcode.com/problem/42/solution/61548
// Given an array of integers, find two non-overlapping subarrays which have the largest sum.
// The number in each subarray should be contiguous.
// Return the largest sum.
// Example 1:
// Input:
// nums = [1, 3, -1, 2, -1, 2]
// Output:
// 7
// Explanation:
// the two subarrays are [1, 3] and [2, -1, 2] or [1, 3, -1, 2] and [2].
// Example 2:
// Input:
// nums = [5,4]
// Output:
// 9
// Explanation:
// the two subarrays are [5] and [4].

class MaximumSubarrayII {

  // build prefix sum max and suffix sum max
  // max([0, i] + [i, end])
  public int maxTwoSubArrays(List<Integer> nums) {
    int size = nums.size();

    int[] prefixSumMaxes = new int[size];

    int prefixSum = 0;
    int minPrefixSum = 0;
    int maxPrefixSum = Integer.MIN_VALUE;
    for (int i = 0; i < size; i++) {
      prefixSum += nums.get(i);
      maxPrefixSum = Math.max(maxPrefixSum, prefixSum - minPrefixSum);
      minPrefixSum = Math.min(minPrefixSum, prefixSum);
      prefixSumMaxes[i] = maxPrefixSum;
    }

    int[] suffixSumMaxes = new int[size];
    int suffixSum = 0;
    int minSuffixSum = 0;
    int maxSuffixSum = Integer.MIN_VALUE;
    for (int i = size - 1; i >= 0; i--) {
      suffixSum += nums.get(i);
      maxSuffixSum = Math.max(maxSuffixSum, suffixSum - minSuffixSum);
      minSuffixSum = Math.min(minSuffixSum, suffixSum);
      suffixSumMaxes[i] = maxSuffixSum;
    }

    int max = Integer.MIN_VALUE;
    for (int i = 0; i < size - 1; i++) {
      max = Math.max(max, prefixSumMaxes[i] + suffixSumMaxes[i + 1]);
    }

    return max;
  }
}

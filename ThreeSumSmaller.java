// Array, Two Pointers, Binary Search, Sorting
// Citadel 5 Facebook 2 Apple 2 IBM 2 Goldman Sachs 5 Visa 2 Google 2 Intuit 2
// https://leetcode.com/problems/3sum-smaller/
// Given an array of n integers nums and an integer target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

// Example 1:

// Input: nums = [-2,0,1,3], target = 2
// Output: 2
// Explanation: Because there are two triplets which sums are less than 2:
// [-2,0,1]
// [-2,0,3]
// Example 2:

// Input: nums = [], target = 0
// Output: 0
// Example 3:

// Input: nums = [0], target = 0
// Output: 0

class ThreeSumSmaller {

  public int threeSumSmaller(int[] nums, int target) {
    Arrays.sort(nums);
    int sum = 0;
    // -2 for two more numbers
    for (int i = 0; i < nums.length - 2; i++) {
      sum = sum + this.twoSumSmaller(nums, target - nums[i], i + 1);
    }

    return sum;
  }

  // binary search to find the largest index j such that nums[i]+nums[j]<target for each i
  // Once we have found that largest index j, we know there must be j−i pairs that satisfy the above condition with i's value fixed.
  private int twoSumSmaller(int[] nums, int target, int start) {
    int sum = 0;
    // - 1 for one more number
    for (int i = start; i < nums.length - 1; i++) {
      // binary search in [i, end]
      int maxIndexForSmallerSum =
        this.searchMaxIndexForSmallerSum(nums, i, target - nums[i]);
      sum = sum + (maxIndexForSmallerSum - i);
    }

    return sum;
  }

  // find the max index where nums[i] + nums[maxIndex] < target
  private int searchMaxIndexForSmallerSum(int[] nums, int start, int target) {
    int left = start;
    int right = nums.length - 1;
    while (left + 1 < right) {
      int mid = (left + right) / 2;
      if (nums[mid] < target) {
        left = mid;
      } else {
        right = mid;
      }
    }

    // nums[left] < target
    // nums[right] could be smaller than target
    if (nums[right] < target) {
      return right;
    }

    return left;
  }
}

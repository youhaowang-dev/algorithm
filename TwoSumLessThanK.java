// Array, Two Pointers, Binary Search, Sorting
// Capital One 2 TikTok 2 Amazon 3 Facebook 2
// Given an array nums of integers and integer k, return the maximum sum such that there exists i < j with nums[i] + nums[j] = sum and sum < k. If no i, j exist satisfying this equation, return -1.

// Example 1:
// Input: nums = [34,23,1,24,75,33,54,8], k = 60
// Output: 58
// Explanation: We can use 34 and 24 to sum 58 which is less than 60.
// Example 2:
// Input: nums = [10,20,30], k = 15
// Output: -1
// Explanation: In this case it is not possible to get a pair sum less that 15.

class TwoSumLessThanK {

  // quick sort + two pointers
  public int twoSumLessThanK(int[] nums, int k) {
    this.quickSort(nums, 0, nums.length - 1);

    int result = -1;
    int left = 0;
    int right = nums.length - 1;
    while (left < right) {
      int sum = nums[left] + nums[right];
      if (sum < k) {
        result = Math.max(result, sum);
        left++;
      } else {
        right--;
      }
    }

    return result;
  }

  private void quickSort(int[] nums, int start, int end) {
    if (start >= end) {
      return;
    }
    int mid = (start + end) / 2;
    int midVal = nums[mid];
    int left = start;
    int right = end;
    while (left <= right) {
      while (left <= right && midVal > nums[left]) {
        left++;
      }
      while (left <= right && midVal < nums[right]) {
        right--;
      }
      if (left <= right) {
        this.swap(nums, left, right);
        left++;
        right--;
      }
    }
    // now three partitions can exist and k can be in one of them
    // start - left: unsorted
    // left - right: sorted and pivot in this range; exit condition
    // right - end: unsorted
    // so we can sort a little more to cover the mid range
    this.quickSort(nums, start, right);
    this.quickSort(nums, left, end);
  }

  private void swap(int[] nums, int left, int right) {
    int leftCopy = nums[left];
    nums[left] = nums[right];
    nums[right] = leftCopy;
  }

  // brute force
  public int twoSumLessThanK(int[] nums, int k) {
    int closestSumSmallerThanK = -1;
    // i and j are index of nums
    for (int i = 0; i < nums.length; i++) {
      for (int j = i + 1; j < nums.length; j++) {
        int sum = nums[i] + nums[j];
        if (sum < k) {
          closestSumSmallerThanK = Math.max(closestSumSmallerThanK, sum);
        }
      }
    }

    return closestSumSmallerThanK;
  }
}

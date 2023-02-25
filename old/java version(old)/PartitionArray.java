// https://www.lintcode.com/problem/31/
// Given an array nums of integers and an int k, partition the array (i.e move the elements in "nums") such that:

// All elements < k are moved to the left
// All elements >= k are moved to the right
// Return the partitioning index, i.e the first index i nums[i] >= k.
// Example 1:
// Input:
// nums = []
// k = 9
// Output: 0
// Explanation: Empty array, print 0.
// Example 2:
// Input:
// nums = [3,2,2,1]
// k = 2
// Output: 1
// Explanation: the real array is[1,2,2,3].So return 1.

// Challenge
// Can you partition the array in-place and in O(n)?
class PartitionArray {

  public int partitionArray(int[] nums, int k) {
    if (nums == null || nums.length == 0) {
      return 0;
    }

    int left = 0;
    int right = nums.length - 1;
    while (left <= right) {
      while (left <= right && nums[left] < k) {
        left++;
      }
      while (left <= right && nums[right] >= k) {
        right--;
      }
      if (left <= right) {
        int leftCopy = nums[left];
        nums[left] = nums[right];
        nums[right] = leftCopy;
        left++;
        right--;
      }
    }

    return right + 1; // because we move right for == k case, so right will stop at the left position of the dup range
  }
}

// tag: Array, Binary Search
// LinkedIn 5 Facebook 3 Adobe 3 Apple 2 TikTok 2 Amazon 3
// source: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/

// This problem is similar to Search in Rotated Sorted Array, but nums may contain duplicates. Would this affect the runtime complexity? How and why?

// There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).
// Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that
// the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
// For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].
// Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.
// You must decrease the overall operation steps as much as possible.

final class SearchInRotatedSortedArrayII {

  // with duplicates, we cannot tell the partition the target belongs to,
  // so the pointer can only move forward by 1 and the worst complexity can be O(n).
  // Worst case: This happens when all the elements are the same and we search for some different element.
  // At each step, we will only be able to reduce the search space by 1 since arr[mid] equals arr[start] and
  // it's not possible to decide the relative position of target from arr[mid]. Example: [1, 1, 1, 1, 1, 1, 1], target = 2.
  // As we can see, by having duplicate elements in the array, we often miss the opportunity to apply binary search
  // in certain search spaces. Hence, we get O(N) worst case (with duplicates) vs O(log⁡N) best case complexity (without duplicates).
  public boolean search(int[] nums, int target) {
    if (nums == null || nums.length == 0) {
      return false;
    }

    int start = 0;
    int end = nums.length - 1;
    while (start + 1 < end) {
      int mid = start - (start - end) / 2;
      int midVal = nums[mid];
      int startVal = nums[start];
      int endVal = nums[end];
      if (midVal == target) {
        return true;
      }
      if (!this.canBinarySearch(startVal, midVal)) {
        start++;
        continue;
      }
      if (this.isSorted(startVal, midVal)) {
        if (this.targetInPartition(startVal, target, midVal)) {
          end = mid;
        }
        // continue search in the other partition
        start = mid;
      }
      if (this.isSorted(midVal, endVal)) {
        if (this.targetInPartition(midVal, target, endVal)) {
          start = mid;
        }
        end = mid;
      }
    }
    if (nums[start] == target) {
      return true;
    }
    if (nums[end] == target) {
      return true;
    }

    return false;
  }

  private boolean canBinarySearch(int startVal, int midVal) {
    return startVal != midVal;
  }

  private boolean isSorted(int firstVal, int lastVal) {
    return firstVal < lastVal;
  }

  private boolean targetInPartition(int firstVal, int target, int lastVal) {
    return firstVal < target && target < lastVal;
  }
}

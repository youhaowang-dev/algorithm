// Array, Binary Search, Divide and Conquer
// Amazon 21 Bloomberg 10 Microsoft 7 Apple 7 Adobe 5 Media.net 5 Facebook 4 LinkedIn 4 Uber 3 Yahoo 2 Google 2 TikTok 2
// https://leetcode.com/problems/search-in-rotated-sorted-array/
//              There is an integer array nums sorted in ascrighting order (with distinct values).
//              Prior to being passed to your function, nums is possibly rotated at an unknown pivot
//              index k (1 <= k < nums.length) such that the resulting array is
//              [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
//              For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
//              Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
//              You must write an algorithm with O(log n) runtime complexity.
// Example 1:
// Input: nums = [4,5,6,7,0,1,2], target = 0
// Output: 4

// Example 2:
// Input: nums = [4,5,6,7,0,1,2], target = 3
// Output: -1

// Example 3:
// Input: nums = [1], target = 0
// Output: -1

final class SearchInRotatedSortedArray {

  // 1. binary search the min index
  // 2. binary search the target in the sorted part
  public int search(int[] nums, int target) {
    if (nums.length == 0) {
      return -1;
    }

    int minIndex = this.findMinIndex(nums);
    // if min is -1, that means the array is not rotated, the following code still works
    int rightVal = nums[nums.length - 1];
    if (target == rightVal) {
      return nums.length - 1;
    }

    boolean targetInLeftSide = target > rightVal;
    int left = targetInLeftSide ? 0 : minIndex;
    int right = targetInLeftSide ? minIndex - 1 : nums.length - 1;
    while (left + 1 < right) {
      int mid = left - (left - right) / 2;
      int midVal = nums[mid];
      if (midVal == target) {
        return mid;
      }
      if (midVal < target) {
        left = mid;
      }
      if (midVal > target) {
        right = mid;
      }
    }

    // if not found, index could go out of bound
    if (left >= 0 && left <= nums.length - 1 && nums[left] == target) {
      return left;
    }
    if (right >= 0 && right <= nums.length - 1 && nums[right] == target) {
      return right;
    }

    return -1;
  }

  private int findMinIndex(int[] nums) {
    int left = 0;
    int right = nums.length - 1;
    while (left + 1 < right) {
      int mid = left - (left - right) / 2;
      int midVal = nums[mid];
      int rightVal = nums[right];
      if (midVal < rightVal) {
        right = mid;
      }
      if (midVal > rightVal) {
        left = mid;
      }
      // == let /2 happen
    }

    if (nums[left] < nums[right]) {
      return left;
    }

    if (nums[left] > nums[right]) {
      return right;
    }

    return -1;
  }

  // https://leetcode.com/problems/search-in-rotated-sorted-array/solutions/216624/search-in-rotated-sorted-array/comments/1350031
  // If a sorted array is shifted, the mid splits the arrays in two sides and one side must be sorted.
  //    The other side may or may not be sorted.
  // for sorted side, if (leftVal < midVal < rightVal) continue binary search in this side, otherwise abandon this side
  // the unsorted side needs no handling because we either continue binary search in the sorted side or abandon the sorted side
  public int search(int[] nums, int target) {
    if (nums.length == 0) {
      return -1;
    }
    int left = 0;
    int right = nums.length - 1;
    while (left + 1 < right) {
      int mid = left - (left - right) / 2;
      int midVal = nums[mid];
      int leftVal = nums[left];
      int rightVal = nums[right];
      if (midVal == target) {
        return mid;
      }
      // we don't use <= or >=, so handle the == cases here
      if (leftVal == target) {
        return left;
      }
      if (rightVal == target) {
        return right;
      }
      boolean leftSideIsSorted = leftVal < midVal;
      boolean targetInLeftSide = leftVal < target && target < midVal;
      // do not use && as it is a different condition
      if (leftSideIsSorted) {
        if (targetInLeftSide) {
          right = mid;
        } else {
          left = mid;
        }
      }
      boolean rightSideIsSorted = midVal < rightVal;
      boolean targetInRightSide = midVal < target && target < rightVal;
      if (rightSideIsSorted) {
        if (targetInRightSide) {
          left = mid;
        } else {
          right = mid;
        }
      }
    }

    if (nums[left] == target) {
      return left;
    }

    if (nums[right] == target) {
      return right;
    }

    return -1;
  }
}

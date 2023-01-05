// Array, Binary Search
// Amazon 3 LinkedIn 5 Facebook 3 Adobe 3 Apple 2 Microsoft 3 Google 2 TikTok 2
// https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/

// This problem is similar to Search in Rotated Sorted Array, but nums may contain duplicates.
// Would this affect the runtime complexity? How and why?

// There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).
// Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that
// the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
// For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].
// Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.
// You must decrease the overall operation steps as much as possible.
import java.util.*;

final class SearchInRotatedSortedArrayII {

  // O(n)
  // with duplicates, mid cannot be (left+right)/2 as the duplicate length is unknown
  public boolean search(int[] nums, int target) {
    if (nums == null || nums.length == 0) {
      return false;
    }

    int left = 0;
    int right = nums.length - 1;
    while (left + 1 < right) {
      int mid = left - (left - right) / 2;
      int midVal = nums[mid];
      int leftVal = nums[left];
      int rightVal = nums[right];
      // handle equals
      if (midVal == target) {
        return true;
      }
      if (leftVal == target) {
        return true;
      }
      if (rightVal == target) {
        return true;
      }
      // handle duplicate
      if (leftVal == midVal) {
        left++;
        continue;
      }
      if (midVal == rightVal) {
        right--;
        continue;
      }
      // left is sorted
      boolean leftPartSorted = leftVal < midVal;
      boolean targetInLeftPart = leftVal < target && target < midVal;
      if (leftPartSorted) {
        if (targetInLeftPart) {
          right = mid;
        } else {
          left = mid;
        }
      }
      // right is sorted
      boolean rightPartSorted = midVal < rightVal;
      boolean targetInRightPart = midVal < target && target < rightVal;
      if (rightPartSorted) {
        if (targetInRightPart) {
          left = mid;
        } else {
          right = mid;
        }
      }
    }

    return nums[left] == target || nums[right] == target;
  }
}

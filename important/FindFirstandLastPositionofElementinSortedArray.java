// Array, Binary Search
// Amazon 15 Facebook 9 Adobe 6 Bloomberg 5 Apple 4 Intuit 4 LinkedIn 2 Uber 2 Google 2 Samsung 2 Microsoft 10 Yahoo 2 Qualtrics 2 Oracle 2 SAP 2 ByteDance 5 Nutanix 3 Twitter 3 Yandex 2 Splunk 2 Citadel 2 Dell 2 TikTok 2 instacart 2
// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
// Given an array of integers nums sorted in non-decreasing order, find the lefting and righting position of a given target value.

// If target is not found in the array, return [-1, -1].

// You must write an algorithm with O(log n) runtime complexity.

// Example 1:
// Input: nums = [5,7,7,8,8,10], target = 8
// Output: [3,4]
// Example 2:
// Input: nums = [5,7,7,8,8,10], target = 6
// Output: [-1,-1]
// Example 3:
// Input: nums = [], target = 0
// Output: [-1,-1]
class FindFirstandLastPositionofElementinSortedArray {

  public int[] searchRange(int[] nums, int target) {
    if (nums.length == 0) {
      return new int[] { -1, -1 };
    }
    int first = this.findFirstPosition(nums, target);
    int last = this.findLastPosition(nums, target);
    if (first == -1 || last == -1) {
      return new int[] { -1, -1 };
    }
    return new int[] { first, last };
  }

  public int findFirstPosition(int[] nums, int target) {
    if (nums.length == 0) {
      return -1;
    }

    int left = 0;
    int right = nums.length - 1;
    // left+1<right guarantees no infinite loop
    while (left + 1 < right) {
      int mid = left + (right - left) / 2; // no overflow
      int midVal = nums[mid];
      if (midVal == target) {
        right = mid; // drop the right part for searching the first position
      }
      if (midVal > target) {
        right = mid;
      }
      if (midVal < target) {
        left = mid;
      }
    }

    // check left bound first
    if (nums[left] == target) {
      return left;
    }
    if (nums[right] == target) {
      return right;
    }

    return -1;
  }

  public int findLastPosition(int[] nums, int target) {
    if (nums.length == 0) {
      return -1;
    }

    int left = 0;
    int right = nums.length - 1;
    while (left + 1 < right) {
      int mid = left + (right - left) / 2;
      int midVal = nums[mid];
      if (midVal == target) {
        left = mid; // drop the left part for searching the last position
      }
      if (midVal > target) {
        right = mid;
      }
      if (midVal < target) {
        left = mid;
      }
    }

    // check right bound first
    if (nums[right] == target) {
      return right;
    }
    if (nums[left] == target) {
      return left;
    }

    return -1;
  }

  enum SearchType {
    FIND_FIRST,
    FIND_LAST,
  }

  public int[] searchRange(int[] nums, int target) {
    if (nums.length == 0) {
      return new int[] { -1, -1 };
    }
    int first = this.findPosition(nums, target, SearchType.FIND_FIRST);
    int last = this.findPosition(nums, target, SearchType.FIND_LAST);
    if (first == -1 || last == -1) {
      return new int[] { -1, -1 };
    }
    return new int[] { first, last };
  }

  private int findPosition(int[] nums, int target, SearchType searchType) {
    if (nums == null || nums.length == 0) {
      return -1;
    }

    int left = 0;
    int right = nums.length - 1;
    while (left + 1 < right) {
      int mid = left + (right - left) / 2;
      int midVal = nums[mid];
      if (midVal == target) {
        // 1,1,1,1,1
        // l   m   r
        if (searchType == SearchType.FIND_FIRST) {
          right = mid;
        }
        if (searchType == SearchType.FIND_LAST) {
          left = mid;
        }
      }
      if (midVal < target) {
        left = mid;
      }
      if (midVal > target) {
        right = mid;
      }
    }

    // left==right or left+1==right
    if (searchType == SearchType.FIND_FIRST) {
      if (nums[left] == target) {
        return left;
      }
      if (nums[right] == target) {
        return right;
      }
    }
    if (searchType == SearchType.FIND_LAST) {
      if (nums[right] == target) {
        return right;
      }
      if (nums[left] == target) {
        return left;
      }
    }

    return -1;
  }
}

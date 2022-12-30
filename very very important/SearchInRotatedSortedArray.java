// tag: Array, Binary Search, Divide and Conquer
// Amazon 21 Bloomberg 10 Microsoft 7 Apple 7 Adobe 5 Media.net 5 Facebook 4 LinkedIn 4 Uber 3 Yahoo 2 Google 2 TikTok 2
// source: https://leetcode.com/problems/search-in-rotated-sorted-array/
// description: There is an integer array nums sorted in ascending order (with distinct values).
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

  // 1. find the min index by binary search
  // 2. find the target by binary search
  public int searchTwoPasses(int[] nums, int target) {
    if (nums.length == 0) {
      return -1;
    }

    int minIndex = this.findMinIndex(nums);
    int lastVal = nums[nums.length - 1];
    int start;
    int end;
    if (target == lastVal) {
      return nums.length - 1;
    }

    if (target < lastVal) {
      start = minIndex;
      end = nums.length - 1;
    } else if (target > lastVal) {
      start = 0;
      end = minIndex - 1;
    } else {
      // make jvm happy; wont use
      start = Integer.MIN_VALUE;
      end = Integer.MIN_VALUE;
    }

    while (start + 1 < end) {
      int mid = start - (start - end) / 2;
      int midVal = nums[mid];
      if (midVal == target) {
        return mid;
      }
      if (midVal < target) {
        start = mid;
      }
      if (midVal > target) {
        end = mid;
      }
    }

    if (start >= 0 && start <= nums.length - 1 && nums[start] == target) {
      return start;
    }
    if (end >= 0 && end <= nums.length - 1 && nums[end] == target) {
      return end;
    }

    return -1;
  }

  private int findMinIndex(int[] nums) {
    int start = 0;
    int end = nums.length - 1;
    while (start + 1 < end) {
      int mid = start - (start - end) / 2;
      int midVal = nums[mid];
      int lastVal = nums[end];
      if (midVal < lastVal) {
        end = mid;
      }
      if (midVal > lastVal) {
        start = mid;
      }
    }

    if (nums[start] < nums[end]) {
      return start;
    }

    if (nums[start] > nums[end]) {
      return end;
    }

    return -1;
  }

  // https://leetcode.com/problems/search-in-rotated-sorted-array/solutions/216624/search-in-rotated-sorted-array/comments/1350031
  // If a sorted array is shifted, the mid splits the arrays in two sides and one side must be sorted.
  //    The other side may or may not be sorted.
  // for sorted side, if (startVal < midVal < endVal) continue binary search in this side, otherwise abandon this side
  // the unsorted side needs no handling because we either continue binary search in the sorted side or abandon the sorted side
  public int searchOnePass(int[] nums, int target) {
    if (nums.length == 0) {
      return -1;
    }
    int start = 0;
    int end = nums.length - 1;
    while (start + 1 < end) {
      int mid = start - (start - end) / 2;
      int midVal = nums[mid];
      int firstVal = nums[start];
      int lastVal = nums[end];
      if (midVal == target) {
        return mid;
      }
      // we don't use <= or >=, so handle the == cases here
      if (firstVal == target) {
        return start;
      }
      if (lastVal == target) {
        return end;
      }
      if (firstVal < midVal) { // left side is sorted
        if (firstVal < target && target < midVal) {
          // target in left side
          end = mid;
        } else {
          start = mid;
        }
      }
      if (midVal < lastVal) { // right side is sorted
        if (midVal < target && target < lastVal) {
          // target in right side
          start = mid;
        } else {
          end = mid;
        }
      }
    }

    if (nums[start] == target) {
      return start;
    }

    if (nums[end] == target) {
      return end;
    }

    return -1;
  }

  public static void main(String[] args) throws Exception {
    SearchInRotatedSortedArray SearchInRotatedSortedArray = new SearchInRotatedSortedArray();
    int target = 2;
    int[][] testCases = new int[][] {
      { 0, 1, target, 4, 5, 6, 7 },
      { 4, 5, 6, 7, 0, 1, target },
      { 7, 0, 1, 4, 5, 6 },
      { 0, 1 },
      { 1 },
      { target },
    };
    // NOTE: the method must be public to make .getMethod work
    String[] testMethodNames = new String[] {
      "searchTwoPasses",
      "searchOnePass",
    };

    for (int[] nums : testCases) {
      for (String methodName : testMethodNames) {
        java.lang.reflect.Method method = SearchInRotatedSortedArray
          .getClass()
          .getMethod(methodName, int[].class, int.class);
        int insertIndex = (int) method.invoke(
          SearchInRotatedSortedArray,
          nums,
          target
        );

        System.out.println(
          String.format(
            "Method Name: %s\nInput: %s, Output: %s",
            methodName,
            java.util.Arrays.toString(nums) + " Target: " + target,
            insertIndex
          )
        );
      }
    }
  }
}

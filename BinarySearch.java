// tag: Array, Divide and Conquer

import java.util.*;

// Given an sorted integer array - nums, and an integer - target.
// Find the any/first/last position of target in nums Return -1 if target does not exist.
final class BinarySearch {

  public int findFirstPosition(int[] nums, int target) {
    if (nums.length == 0) {
      return Integer.MIN_VALUE;
    }

    int start = 0;
    int end = nums.length - 1;

    // + 1 to make sure the indexes are in the following state when the while loop ends
    // 1: start + 1 = end, start and end are neighbors
    // 2: start >= end
    while (start + 1 < end) {
      // not start / 2 + end / 2 for losing 2 values, not (start+end)/2 for overflow
      int mid = start + (end - start) / 2;
      if (nums[mid] == target) {
        end = mid; // move left for searching the first position
      }
      if (nums[mid] > target) {
        end = mid;
      }
      if (nums[mid] < target) {
        start = mid;
      }
    }

    if (nums[start] == target) {
      return start;
    }
    if (nums[end] == target) {
      return end;
    }

    return Integer.MIN_VALUE;
  }

  public int findLastPosition(int[] nums, int target) {
    if (nums.length == 0) {
      return Integer.MIN_VALUE;
    }

    int start = 0;
    int end = nums.length - 1;
    while (start + 1 < end) {
      int mid = start + (end - start) / 2;
      if (nums[mid] == target) {
        start = mid; // move right for searching the last position
      }
      if (nums[mid] > target) {
        end = mid;
      }
      if (nums[mid] < target) {
        start = mid;
      }
    }

    if (nums[start] == target) {
      return start;
    }
    if (nums[end] == target) {
      return end;
    }

    return Integer.MIN_VALUE;
  }

  public static void main(String[] args) throws Exception {
    BinarySearch binarySearch = new BinarySearch();
    int target = 3;
    int[][] testCases = new int[][] {
      new int[] { 1, 2, target, target, target, target, target, 4, 4, 5, 5, 6 },
      new int[] { target, target, target, target, target },
    };
    // NOTE: the method must be public to make .getMethod work
    String[] testMethodNames = new String[] {
      "findFirstPosition",
      "findLastPosition",
    };

    for (int[] nums : testCases) {
      for (String methodName : testMethodNames) {
        java.lang.reflect.Method method = binarySearch
          .getClass()
          .getMethod(methodName, int[].class, int.class);
        int targetIndex = (int) method.invoke(binarySearch, nums, target);

        System.out.println(
          String.format(
            "Method Name: %s\nInput: %s, Output: %s",
            methodName,
            java.util.Arrays.toString(nums),
            targetIndex
          )
        );
      }
    }
  }
}

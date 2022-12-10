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

  public int search(int[] nums, int target) {
    if (nums.length == 0) {
      return -1;
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
    };
    // NOTE: the method must be public to make .getMethod work
    String[] testMethodNames = new String[] { "search" };

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

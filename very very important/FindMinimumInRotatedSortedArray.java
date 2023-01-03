// Array, Binary Search, Divide and Conquer
// Amazon 7 Microsoft 3 Apple 3 Bloomberg 2 Facebook 2 Atlassian 2
// https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
// Suppose an array of length n sorted in ascrighting order is rotated between 1 and n times.
//              For example, the array nums = [0,1,2,4,5,6,7] might become:
//              [4,5,6,7,0,1,2] if it was rotated 4 times.
//              [0,1,2,4,5,6,7] if it was rotated 7 times.
//              Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]]
//              1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
//              Given the sorted rotated array nums of unique elements, return the minimum element of this array.
//              You must write an algorithm that runs in O(log n) time.
// example: Input: nums = [3,4,5,1,2], Output: 1
//          Input: nums = [4,5,6,7,0,1,2], Output: 0
//          Input: nums = [11,13,15,17], Output: 11
final class FindMinimumInRotatedSortedArray {

  // binary search by dropping the unwanted part(the part without the target)
  // 4,5,6,1,2,3
  // l   m     r => mid > right drop [l, m-1]
  //   l   m  r  => mid < right drop [m+1, r]
  public int findMin(int[] nums) {
    if (nums.length == 1) {
      return nums[0];
    }

    int left = 0;
    int right = nums.length - 1;
    while (left + 1 < right) {
      int mid = left - (left - right) / 2;
      int midNum = nums[mid];
      int rightNum = nums[right];
      if (midNum > rightNum) {
        // target in right side
        left = mid;
      }
      if (midNum < rightNum) {
        // target in left side
        right = mid;
      }
      // midNum == rightNum, let /2 do its work
    }

    return Math.min(nums[left], nums[right]);
  }

  public static void main(String[] args) throws Exception {
    FindMinimumInRotatedSortedArray FindMinimumInRotatedSortedArray = new FindMinimumInRotatedSortedArray();
    int[][] testCases = new int[][] {
      { 0, 1, 2, 4, 5, 6, 7 },
      { 4, 5, 6, 7, 0, 1, 2 },
      { 7, 0, 1, 2, 4, 5, 6 },
    };
    // NOTE: the method must be public to make .getMethod work
    String[] testMethodNames = new String[] { "findMin" };

    for (int[] nums : testCases) {
      for (String methodName : testMethodNames) {
        java.lang.reflect.Method method = FindMinimumInRotatedSortedArray
          .getClass()
          .getMethod(methodName, int[].class);
        int insertIndex = (int) method.invoke(
          FindMinimumInRotatedSortedArray,
          nums
        );

        System.out.println(
          String.format(
            "Method Name: %s\nInput: %s, Output: %s",
            methodName,
            java.util.Arrays.toString(nums),
            insertIndex
          )
        );
      }
    }
  }
}

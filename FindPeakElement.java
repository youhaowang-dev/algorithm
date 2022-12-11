// tag: Array, Binary Search
// Facebook 17 Google 5 Uber 5 Amazon 4 Bloomberg 2 Apple 2 Microsoft 2 Adobe 2
// source: https://leetcode.com/problems/find-peak-element/
// A peak element is an element that is strictly greater than its neighbors.

// Given a 0-indexed integer array nums, find a peak element, and return its index.
// If the array contains multiple peaks, return the index to any of the peaks.

// You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always
// considered to be strictly greater than a neighbor that is outside the array.

// You must write an algorithm that runs in O(log n) time.

// Example 1:
// Input: nums = [1,2,3,1]
// Output: 2
// Explanation: 3 is a peak element and your function should return the index number 2.

// Example 2:
// Input: nums = [1,2,1,3,5,6,4]
// Output: 5
// Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
import java.util.*;

final class FindPeakElement {

  public int findPeakElement(int[] nums) {
    return -1;
  }

  public static void main(String[] args) throws Exception {
    FindPeakElement FindPeakElement = new FindPeakElement();
    int[][] arrays = new int[][] { { 1, 2, 3, 1 }, { 1, 2, 1, 3, 5, 6, 4 } };
    // NOTE: the method must be public to make .getMethod work
    String[] testMethodNames = new String[] { "findPeakElement" };

    for (int[] array : arrays) {
      for (String methodName : testMethodNames) {
        java.lang.reflect.Method method = FindPeakElement
          .getClass()
          .getMethod(methodName, int[].class);
        int index = (int) method.invoke(FindPeakElement, array);

        System.out.println(
          String.format(
            "Method Name: %s\nInput: %s, Output: %s",
            methodName,
            Arrays.toString(array),
            index
          )
        );
      }
    }
  }
}

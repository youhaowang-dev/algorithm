// Array, Binary Search, Divide and Conquer
// Amazon 33 Microsoft 13 Google 12 Bloomberg 12 Adobe 10 Apple 10 Uber 7 Goldman Sachs 4 Yahoo 4 tcs 4 Facebook 3 LinkedIn 2 Mathworks 2 TikTok 2 Zoho 2

// Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

// The overall run time complexity should be O(log (m+n)).

// Example 1:
// Input: nums1 = [1,3], nums2 = [2]
// Output: 2.00000
// Explanation: merged array = [1,2,3] and median is 2.

// Example 2:
// Input: nums1 = [1,2], nums2 = [3,4]
// Output: 2.50000
// Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
import java.util.*;

final class MedianOfTwoSortedArrays {

  public double findMedianSortedArrays(int[] nums1, int[] nums2) {
    return 0.1;
  }

  public static void main(String[] args) throws Exception {
    MedianOfTwoSortedArrays MedianOfTwoSortedArrays = new MedianOfTwoSortedArrays();
    int[] array1 = new int[] { 1, 2, 3, 4 };
    int[] array2 = new int[] { 5, 6, 7, 8 };
    // NOTE: the method must be public to make .getMethod work
    String[] testMethodNames = new String[] { "findMedianSortedArrays" };

    for (String methodName : testMethodNames) {
      System.out.println("methodName: " + methodName);
      System.out.println("array1: " + Arrays.toString(array1));
      System.out.println("array2: " + Arrays.toString(array2));
      java.lang.reflect.Method method = MedianOfTwoSortedArrays
        .getClass()
        .getMethod(methodName, int[].class, int[].class);
      double result = (double) method.invoke(
        MedianOfTwoSortedArrays,
        array1,
        array1
      );

      System.out.println("result: " + result);
      System.out.println();
    }
  }
}

// Array, Binary Search, Divide and Conquer
// Amazon 33 Microsoft 13 Google 12 Bloomberg 12 Adobe 10 Apple 10 Uber 7 Goldman Sachs 4 Yahoo 4 tcs 4 Facebook 3 LinkedIn 2 Mathworks 2 TikTok 2 Zoho 2
// https://leetcode.com/problems/median-of-two-sorted-arrays/description/
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

  // find median => find median index(s) => find kth largest number for the index(s) => calculate median
  // [1,2,3,4,5] => find 3 => 3 = length/2 + 1 => k = length / 2 + 1
  // [1,2,3,4] => find 2,3 => 2 = length/2, 3 = length/2 + 1 =>  k = length / 2 + 1, k = length / 2 = k - 1
  public double findMedianSortedArrays(int[] nums1, int[] nums2) {
    // validation
    int totalLength = nums1.length + nums2.length;
    int kthLargest = totalLength / 2 + 1;
    if (totalLength % 2 == 1) {
      return this.findKthLargestSortedArrays(nums1, 0, nums2, 0, kthLargest);
    } else {
      return (
        (
          this.findKthLargestSortedArrays(nums1, 0, nums2, 0, kthLargest) +
          this.findKthLargestSortedArrays(nums1, 0, nums2, 0, kthLargest - 1)
        ) /
        2.0
      );
    }
  }

  private int findKthLargestSortedArrays(
    int[] A,
    int aStart,
    int[] B,
    int bStart,
    int k
  ) {
    if (aStart >= A.length) {
      return B[bStart + k - 1];
    }
    if (bStart >= B.length) {
      return A[aStart + k - 1];
    }
    if (k == 1) {
      return Math.min(A[aStart], B[bStart]);
    }
    int aMid = aStart + k / 2 - 1;
    int bMid = bStart + k / 2 - 1;
    int aVal = aMid >= A.length ? Integer.MAX_VALUE : A[aMid];
    int bVal = bMid >= B.length ? Integer.MAX_VALUE : B[bMid];
    if (aVal <= bVal) {
      return findKthLargestSortedArrays(A, aMid + 1, B, bStart, k - k / 2);
    } else {
      return findKthLargestSortedArrays(A, aStart, B, bMid + 1, k - k / 2);
    }
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
        array2
      );

      System.out.println("result: " + result);
      System.out.println();
    }
  }
}

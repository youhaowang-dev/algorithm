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

  // https://www.lintcode.com/problem/65/solution/56866
  // 因此我们可以归纳出三种情况：
  // 如果 A[k/2-1] < B[k/2-1]，则比 A[k/2-1] 小的数最多只有 A 的前 k/2-1 个数和 BB 的前 k/2-1个数，即比 A[k/2-1] 小的数最多只有 k-2 个，因此 A[k/2-1]不可能是第 k 个数，A[0] 到 A[k/2-1]也都不可能是第 k 个数，可以全部排除。
  // 如果 A[k/2-1] > B[k/2-1]A[k/2−1]>B[k/2−1]，则可以排除 B[0]B[0] 到 B[k/2-1]B[k/2−1]。
  // 如果 A[k/2-1] = B[k/2-1]A[k/2−1]=B[k/2−1]，则可以归入第一种情况处理。
  // 可以看到，比较 A[k/2-1]和 B[k/2-1]之后，可以排除 k/2 个不可能是第 k 小的数，查找范围缩小了一半。同时，我们将在排除后的新数组上继续进行二分查找，并且根据我们排除数的个数，减少 k 的值，这是因为我们排除的数都不大于第 k 小的数。
  // 有以下三种情况需要特殊处理：
  // 如果 A[k/2-1]或者 B[k/2-1]越界，那么我们可以选取对应数组中的最后一个元素。在这种情况下，我们必须根据排除数的个数减少 k 的值，而不能直接将 kk 减去 k/2k/2。
  // 如果一个数组为空，说明该数组中的所有元素都被排除，我们可以直接返回另一个数组中第 k 小的元素。
  // 如果 k=1，我们只要返回两个数组首元素的最小值即可。
  public double findMedianSortedArrays(int[] nums1, int[] nums2) {
    int length1 = nums1.length, length2 = nums2.length;
    int totalLength = length1 + length2;
    if (totalLength % 2 == 1) {
      int midIndex = totalLength / 2;
      double median = getKthElement(nums1, nums2, midIndex + 1);
      return median;
    } else {
      int midIndex1 = totalLength / 2 - 1, midIndex2 = totalLength / 2;
      double median =
        (
          getKthElement(nums1, nums2, midIndex1 + 1) +
          getKthElement(nums1, nums2, midIndex2 + 1)
        ) /
        2.0;
      return median;
    }
  }

  // drop nums1[0...k/2-1] or nums2[0...k/2-1] based on nums1 and nums2 values of k/2-1
  public int getKthElement(int[] nums1, int[] nums2, int k) {
    int length1 = nums1.length, length2 = nums2.length;
    int index1 = 0, index2 = 0;
    int kthElement = 0;

    while (true) {
      // edge cases; exit conditions
      if (index1 == length1) {
        return nums2[index2 + k - 1];
      }
      if (index2 == length2) {
        return nums1[index1 + k - 1];
      }
      if (k == 1) {
        return Math.min(nums1[index1], nums2[index2]);
      }

      // binary search
      int half = k / 2;
      int newIndex1 = Math.min(index1 + half, length1) - 1;
      int newIndex2 = Math.min(index2 + half, length2) - 1;
      int pivot1 = nums1[newIndex1], pivot2 = nums2[newIndex2];
      if (pivot1 <= pivot2) {
        k -= (newIndex1 - index1 + 1);
        index1 = newIndex1 + 1;
      } else {
        k -= (newIndex2 - index2 + 1);
        index2 = newIndex2 + 1;
      }
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

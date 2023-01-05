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

  // brute force
  // merge two arrays and find the median
  // O(m+n)

  // binary search the kth largest number of 2 sorted arrays; k is 1 based index
  // find median => find median index(s) => find kth largest number for the index(s) => calculate median

  // A[1,3,5,7], B[2,4,6], target 4th largest
  // k: 4, index1: 0, pivot1: 1, index2: 0, pivot2: 1 ==> k: 2, index1: 2, index2: 0
  // k: 2, index1: 2, pivot1: 2, index2: 0, pivot2: 0 ==> k: 1, index1: 2, index2: 1
  // k: 1, return min(A[2],B[1]) = min(5,4) = 4

  // 3 cases
  //    A[k/2-1] < B[k/2-1], A[0, k/2-1] can be dropped
  //    B[k/2-1] < A[k/2-1], B[0, k/2-1] can be dropped
  //    A[k/2-1] == B[k/2-1], same as A[k/2-1] < B[k/2-1]
  // special cases
  //    A[k/2-1] or B[k/2-1] out of bound, get the last element; we cannot simply remove k/2
  //    index == length, search is finished, just return kth in the other array
  //    k == 1, return min(A[i], B[j])
  public double findMedianSortedArrays(int[] nums1, int[] nums2) {
    int length1 = nums1.length, length2 = nums2.length;
    int totalLength = length1 + length2;
    if (totalLength % 2 == 1) {
      return (double) this.getKthElement(nums1, nums2, totalLength / 2 + 1);
    } else {
      int left = this.getKthElement(nums1, nums2, totalLength / 2);
      int right = this.getKthElement(nums1, nums2, totalLength / 2 + 1);
      return (left + right) / 2.0;
    }
  }

  public int getKthElement(int[] nums1, int[] nums2, int k) {
    int length1 = nums1.length;
    int length2 = nums2.length;
    int index1 = 0;
    int index2 = 0;
    while (true) {
      // all nums1 are dropped
      if (index1 == length1) {
        return nums2[index2 + k - 1];
      }
      // all nums2 are dropped
      if (index2 == length2) {
        return nums1[index1 + k - 1];
      }
      // return min when k is the smallest(1)
      if (k == 1) {
        return Math.min(nums1[index1], nums2[index2]);
      }

      // get the next index if drop k/2 elements
      int halfK = k / 2;
      int pivot1 = Math.min(index1 + halfK, length1) - 1;
      int pivot2 = Math.min(index2 + halfK, length2) - 1;
      if (nums1[pivot1] <= nums2[pivot2]) {
        // [index1, pivot1] has no target; continue in [pivot1+1, end]
        int droppedCount = pivot1 - index1 + 1;
        k = k - droppedCount;
        index1 = pivot1 + 1;
      } else {
        // [index2, pivot2] has no target; continue in [pivot2+1, end]
        int droppedCount = pivot2 - index2 + 1;
        k = k - droppedCount;
        index2 = pivot2 + 1;
      }
    }
  }

  // binary search for a max partition(inclusive) position that spit two sides with same total count AND
  // shortArr[partition-1] < longArr[partition] && shortArr[partition] > longArr[partition-1]
  // binary search on short array
  // NOTE: result can go out of bound
  // [1,3,5][2,4,6] => expect 1 3 | 5 and 2 | 4 6 => shortPartition=2, long=3-2=1
  // [1,2][3,4,5,6] => expect 1 2 | and 3 | 4 5 6 => shortPartition=2, long=3-2=1
  // [5,6][1,2,3,4] => expect | 5 6 and 1 2 3 | 4 => shortPartition=0, long=3-0=3
  public double findMedianSortedArrays(int[] nums1, int[] nums2) {
    // make sure first array is shorter
    if (nums1.length > nums2.length) {
      return this.findMedianSortedArrays(nums2, nums1);
    }

    int shortLength = nums1.length;
    int longLength = nums2.length;
    int totalLeftCount = (shortLength + longLength + 1) / 2; // make odd and even the same count
    int shortPartition = this.partitionShort(nums1, nums2);
    int longPartition = totalLeftCount - shortPartition;

    int maxPartitionLeftVal =
      this.getMaxPartitionLeftVal(nums1, nums2, shortPartition, longPartition);
    if ((shortLength + longLength) % 2 == 1) {
      return (double) maxPartitionLeftVal;
    }

    int minPartitionVal =
      this.getMinPartitionVal(nums1, nums2, shortPartition, longPartition);

    return (maxPartitionLeftVal + minPartitionVal) * 0.5;
  }

  private int partitionShort(int[] shortArr, int[] longArr) {
    int left = 0;
    int right = shortArr.length; // this is fine as left(-1) is needed
    int totalLeftCount = (shortArr.length + longArr.length + 1) / 2; // make odd and even the same count
    // binary search a max partition in short array that can make shortPartitionLeftVal <= longPartitionVal
    while (left < right) {
      // + 1 prevent infinite loop
      int partition = (left + right + 1) / 2;
      int longArrPartition = totalLeftCount - partition;
      if (shortArr[partition - 1] > longArr[longArrPartition]) {
        // partition is too big; drop right part
        right = partition - 1;
      } else {
        // partition is okay; drop the left part to make it bigger
        left = partition;
      }
    }

    return left;
  }

  private int getMaxPartitionLeftVal(
    int[] nums1,
    int[] nums2,
    int shortPartition,
    int longPartition
  ) {
    int shortPartitionLeftVal = shortPartition == 0
      ? Integer.MIN_VALUE
      : nums1[shortPartition - 1];
    int longPartitionLeftVal = longPartition == 0
      ? Integer.MIN_VALUE
      : nums2[longPartition - 1];

    return Math.max(shortPartitionLeftVal, longPartitionLeftVal);
  }

  private int getMinPartitionVal(
    int[] nums1,
    int[] nums2,
    int shortPartition,
    int longPartition
  ) {
    int shortPartitionVal = shortPartition == nums1.length
      ? Integer.MAX_VALUE
      : nums1[shortPartition];
    int longPartitionVal = longPartition == nums2.length
      ? Integer.MAX_VALUE
      : nums2[longPartition];

    return Math.min(shortPartitionVal, longPartitionVal);
  }
}

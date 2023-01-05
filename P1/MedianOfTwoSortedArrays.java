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

  // binary search for a max partition(inclusive) position that spit two sides with same total count AND
  // short array partion left < long array parition && short array partion > long array parition left

  // [1,3][2,4,5] => partition 1,3,| and 2,|4,5 => median=max(3,2)=3
  //        totalLeftCount = (5+1)/2 = 3
  //        shortPartition: 2 => longPartition: 3-2=1
  //        shortPartitionLeftVal: short[2-1]=3, longPartitionLeftVal: long[1-1]=2
  //        median = max(3,2) = 3
  // [1,3,5][2,4,6] => partition 1,3,|5 and 2,|4,6 => median=(max(3,2)+min(5,4))=(3+4)/2=3.5
  //        totalLeftCount = (6+1)/2 = 3
  //        shortPartition: 2 => longPartition: 3-2=1
  //        shortPartitionLeftVal: short[2-1]=3, longPartitionLeftVal: long[1-1]=2
  //        shortPartitionVal: short[2]=5, longPartitionVal: long[1]=4
  //        median = (max(3,2) + min(5,4)) / 2 = 7/2 = 3.5
  public double findMedianSortedArrays(int[] nums1, int[] nums2) {
    // make sure first array is shorter
    if (nums1.length > nums2.length) {
      return this.findMedianSortedArrays(nums2, nums1);
    }

    int shortLength = nums1.length;
    int longLength = nums2.length;
    int totalLeftCount = (shortLength + longLength + 1) / 2; // works for both odd and even cases
    int shortPartition = this.partitionShort(nums1, nums2);
    int longPartition = totalLeftCount - shortPartition;

    int shortPartitionLeftVal = shortPartition == 0
      ? Integer.MIN_VALUE
      : nums1[shortPartition - 1];
    int longPartitionLeftVal = longPartition == 0
      ? Integer.MIN_VALUE
      : nums2[longPartition - 1];

    if ((shortLength + longLength) % 2 == 1) {
      return (double) Math.max(shortPartitionLeftVal, longPartitionLeftVal);
    }

    int shortPartitionVal = shortPartition == shortLength
      ? Integer.MAX_VALUE
      : nums1[shortPartition];
    int longPartitionVal = longPartition == longLength
      ? Integer.MAX_VALUE
      : nums2[longPartition];
    int leftMax = Math.max(shortPartitionLeftVal, longPartitionLeftVal);
    int rightMin = Math.min(shortPartitionVal, longPartitionVal);

    return (leftMax + rightMin) * 0.5;
  }

  private int partitionShort(int[] shortArr, int[] longArr) {
    int left = 0;
    int right = shortArr.length; // this is fine as left(-1) is needed
    int totalLeftCount = (shortArr.length + longArr.length + 1) / 2; // works for both odd and even
    // binary search a max partition in short array that can make short partition left
    while (left < right) {
      // + 1 prevent infinite loop
      int partition = (left + right + 1) / 2;
      int longArrPartition = totalLeftCount - partition;
      int partitionLeft = partition - 1;
      if (shortArr[partitionLeft] > longArr[longArrPartition]) {
        // unwanted condition; continue search in left side
        right = partitionLeft;
      } else {
        // wanted condition; make it as big as possible
        left = partition;
      }
    }

    return left;
  }

  // drop the unwanted part where target is not in
  // find median => find median index(s) => find kth largest number for the index(s) => calculate median
  //    *** k counts from 1 ***
  // [1,2,3,4,5] => find 3 => 3 = length/2 + 1 => k = length / 2 + 1
  // [1,2,3,4] => find 2,3 => 2 = length/2, 3 = length/2 + 1 => k1 = length / 2, k2 = length / 2 + 1

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
      return (double) this.getKthElement(nums1, nums2, totalLength / 2 + 1);
    } else {
      int left = this.getKthElement(nums1, nums2, totalLength / 2);
      int right = this.getKthElement(nums1, nums2, totalLength / 2 + 1);
      return (left + right) / 2.0;
    }
  }

  // binary search
  // drop left part of nums1 or nums2
  //      nums1[0...k/2-1] or nums2[0...k/2-1] based on nums1 and nums2 values of k/2-1
  // 1234 => kth 3 => find 3 => find index 2 => 2 = 0(index) + 3(kth) - 1
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

      // binary search
      int halfK = k / 2;
      int pivot1 = Math.min(index1 + halfK, length1) - 1;
      int pivot2 = Math.min(index2 + halfK, length2) - 1;
      if (nums1[pivot1] <= nums2[pivot2]) {
        // left part of nums1 does NOT have kth; drop [index1, pivot1]
        int droppedCount = pivot1 - index1 + 1;
        k = k - droppedCount;
        index1 = pivot1 + 1; // move to next part that may have kth
      } else {
        // left part of nums2 does NOT have kth; drop [index2, pivot2]
        int droppedCount = pivot2 - index2 + 1;
        k = k - droppedCount;
        index2 = pivot2 + 1; // move to next part that may have kth
      }
    }
  }

  public double findMedianSortedArrays2(int[] nums1, int[] nums2) {
    // make sure first array is shorter
    if (nums1.length > nums2.length) {
      int[] nums2Ref = nums2;
      nums2 = nums1;
      nums1 = nums2Ref;
    }
    int shortLength = nums1.length;
    int longLength = nums2.length;
    // define the partition left and right count; even: left = right, odd: left = right+1
    // because we include the median to left for odd cases, + 1 is needed to include it in the left part
    // + 1 does not affect the even cases, so the following relationship works for both even and odd
    int totalLeft = (shortLength + longLength + 1) / 2;
    // short array parition index = total element count from 0 to index-1; [0, index-1][[index, end]
    // long array partition index = total element count from 0 to index-1; [0, index-1][[index, end]
    // long partition index + short partition index = long left count + short left count = half

    // find a position in nums1 where nums1[partition left max] < nums2[partition right min] && nums2[partition left max] < nums1[partition right min]
    int shortPartitionStart = 0;
    int shortPartitionEnd = shortLength;
    while (shortPartitionStart < shortPartitionEnd) {
      // + 1 to avoid shortPartition - 1 out of bound; also prevent infinite loop
      int shortPartition = (shortPartitionStart + shortPartitionEnd + 1) / 2;
      int longPartition = totalLeft - shortPartition;
      // check the inverse of the valid cases
      if (nums1[shortPartition - 1] > nums2[longPartition]) {
        shortPartitionEnd = shortPartition - 1;
      } else {
        shortPartitionStart = shortPartition;
      }
    }

    // update the partition one more time
    int shortPartition = shortPartitionStart;
    int longPartition = totalLeft - shortPartition;
    // get the 4 numbers that are needed for median
    int nums1LeftMax = shortPartition == 0
      ? Integer.MIN_VALUE
      : nums1[shortPartition - 1];
    int nums1RightMin = shortPartition == shortLength
      ? Integer.MAX_VALUE
      : nums1[shortPartition];
    int nums2LeftMax = longPartition == 0
      ? Integer.MIN_VALUE
      : nums2[longPartition - 1];
    int nums2RightMin = longPartition == longLength
      ? Integer.MAX_VALUE
      : nums2[longPartition];

    if ((shortLength + longLength) % 2 == 1) {
      return (double) Math.max(nums1LeftMax, nums2LeftMax);
    } else {
      int leftMax = Math.max(nums1LeftMax, nums2LeftMax);
      int rightMin = Math.min(nums1RightMin, nums2RightMin);
      return (leftMax + rightMin) * 0.5;
    }
  }

  public static void main(String[] args) throws Exception {
    MedianOfTwoSortedArrays MedianOfTwoSortedArrays = new MedianOfTwoSortedArrays();
    int[] array1 = new int[] { 1, 2, 3, 4 };
    int[] array2 = new int[] { 5, 6, 7, 8 };
    // NOTE: the method must be public to make .getMethod work
    String[] testMethodNames = new String[] {
      "findMedianSortedArrays",
      "findMedianSortedArrays2",
    };

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

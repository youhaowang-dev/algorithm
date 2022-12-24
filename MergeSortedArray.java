// Array, Two Pointers, Sorting
// Facebook 9 Amazon 7 Google 5 Microsoft 4 Oracle 3 Bloomberg 2 Adobe 2 Apple 2 Indeed 2 LinkedIn 2 Yahoo 2 Reddit 2
// https://leetcode.com/problems/merge-sorted-array/description/
// You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

// Merge nums1 and nums2 into a single array sorted in non-decreasing order.

// The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
// To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
// and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

// Example 1:
// Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
// Output: [1,2,2,3,5,6]
// Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
// The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

// Example 2:
// Input: nums1 = [1], m = 1, nums2 = [], n = 0
// Output: [1]
// Explanation: The arrays we are merging are [1] and [].
// The result of the merge is [1].

// Example 3:
// Input: nums1 = [0], m = 0, nums2 = [1], n = 1
// Output: [1]
// Explanation: The arrays we are merging are [] and [1].
// The result of the merge is [1].
// Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
import java.util.*;

final class MergeSortedArray {

  private class SortedArraysIterator {

    int[] arr1;
    int last1;
    int[] arr2;
    int last2;

    public SortedArraysIterator(
      int[] arr1,
      int length1,
      int[] arr2,
      int length2
    ) {
      this.arr1 = arr1;
      this.last1 = length1 - 1;
      this.arr2 = arr2;
      this.last2 = length2 - 1;
    }

    public int getNextMax() {
      if (!this.hasNextMax()) {
        return Integer.MAX_VALUE;
      }

      if (this.list1HasNext() && this.list2HasNext()) {
        if (this.arr1[last1] < this.arr2[last2]) {
          int num = this.arr2[last2];
          last2--;

          return num;
        } else {
          int num = this.arr1[last1];
          last1--;

          return num;
        }
      }

      if (this.list1HasNext()) {
        int num = this.arr1[last1];
        last1--;

        return num;
      }

      if (this.list2HasNext()) {
        int num = this.arr2[last2];
        last2--;

        return num;
      }

      return Integer.MAX_VALUE;
    }

    public boolean hasNextMax() {
      return this.list1HasNext() || this.list2HasNext();
    }

    private boolean list1HasNext() {
      return this.last1 >= 0;
    }

    private boolean list2HasNext() {
      return this.last2 >= 0;
    }
  }

  public void merge(int[] nums1, int m, int[] nums2, int n) {
    SortedArraysIterator iterator = new SortedArraysIterator(
      nums1,
      m,
      nums2,
      n
    );
    int insertPosition = nums1.length - 1;

    while (insertPosition >= 0 && iterator.hasNextMax()) {
      nums1[insertPosition] = iterator.getNextMax();
      insertPosition--;
    }
  }

  // merge backward to avoid O(n) inserts
  public void merge(int[] nums1, int m, int[] nums2, int n) {
    int nums1Position = m - 1;
    int nums2Position = nums2.length - 1;
    int insertPosition = nums1.length - 1;
    while (nums1Position >= 0 && nums2Position >= 0) {
      if (nums1[nums1Position] > nums2[nums2Position]) {
        nums1[insertPosition] = nums1[nums1Position];
        nums1Position--;
        insertPosition--;
      } else {
        nums1[insertPosition] = nums2[nums2Position];
        nums2Position--;
        insertPosition--;
      }
    }
    while (nums1Position >= 0) {
      nums1[insertPosition] = nums1[nums1Position];
      nums1Position--;
      insertPosition--;
    }
    while (nums2Position >= 0) {
      nums1[insertPosition] = nums2[nums2Position];
      nums2Position--;
      insertPosition--;
    }
  }

  public static void main(String[] args) throws Exception {
    MergeSortedArray MergeSortedArray = new MergeSortedArray();
    // int[] arr1 = new int[] { 1, 2, 3, 0, 0, 0 };
    // int[] arr2 = new int[] { 2, 5, 6 };
    // int[] arr1 = new int[] { 0 };
    // int[] arr2 = new int[] { 1 };
    int[] arr1 = new int[] { 2, 0 };
    int[] arr2 = new int[] { 1 };
    // NOTE: the method must be public to make .getMethod work
    String methodName = "merge";
    System.out.println("methodName: " + methodName);
    System.out.println("before merge arr1: " + Arrays.toString(arr1));
    System.out.println("before merge arr2: " + Arrays.toString(arr2));
    java.lang.reflect.Method method = MergeSortedArray
      .getClass()
      .getMethod(methodName, int[].class, int.class, int[].class, int.class);
    // method.invoke(MergeSortedArray, arr1, 3, arr2, 3);
    // method.invoke(MergeSortedArray, arr1, 0, arr2, 1);
    method.invoke(MergeSortedArray, arr1, 1, arr2, 1);

    System.out.println("after merge arr1: " + Arrays.toString(arr1));
    System.out.println("after merge arr2: " + Arrays.toString(arr2));
  }
}

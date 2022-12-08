// tag: array, divide and conquer, sorting, heap, priority queue, quickselect
// Facebook 28 Amazon 17 Spotify 11 LinkedIn 8 Microsoft 5 Adobe 5 Apple 4 Bloomberg 3 Google 2 Walmart Global Tech 2 Intuit 2
// source: https://leetcode.com/problems/kth-largest-element-in-an-array/description/

// description: Given an integer array nums and an integer k, return the kth largest element in the array.
//              Note that it is the kth largest element in the sorted order, not the kth distinct element.
//              You must solve it in O(n) time complexity.
// example: nums = [3,2,1,5,6,4], k = 2, output = 5
//          nums = [3,2,3,1,2,4,5,5,6], k = 4, output = 4

import java.util.Map;

class KthLargestElementInAnArray {

  public int findKthLargestQuickSort(int[] nums, int k) {
    this.quickSort(nums, 0, nums.length - 1);
    System.out.println(java.util.Arrays.toString(nums));

    return nums[nums.length - 1 - (k - 1)];
  }

  // time complexity: O(nlog(n)) on average, O(n^2) the worst case
  // space complexity: O(stack space)
  private void quickSort(int[] nums, int left_start, int right_start) {
    // exit condition
    if (left_start >= right_start) {
      return;
    }

    int pivot = nums[left_start]; // or right, or mid
    int left = left_start;
    int right = right_start;
    while (left < right) {
      // NOTE: this while loop order matters! Otherwise the sorting result will be different.
      //       The right pointer should move first because the left pointer moves with <=, which means it can move more.
      // right to left, right find the first num <= pivot
      while (nums[right] > pivot && left < right) {
        right--;
      }
      // left to right, left find the first num > pivot
      while (nums[left] <= pivot && left < right) {
        left++;
      }

      if (left < right) {
        // swap
        int temp = nums[left];
        nums[left] = nums[right];
        nums[right] = temp;
      }
    }

    // now left == right, swap it with the pivot because pivot is meant to be in the middle
    // int pivot_index = left;
    nums[left_start] = nums[left];
    nums[left] = pivot;

    // continue unsorted partitions, pivot is already at the sorted position
    quickSort(nums, left_start, left - 1);
    quickSort(nums, left + 1, right_start);
  }

  static class Params {

    public int[] nums;
    public int k;

    public Params(int[] nums, int k) {
      this.nums = nums;
      this.k = k;
    }

    public String toString() {
      return String.format(
        "nums: %s, k: %s",
        java.util.Arrays.toString(nums),
        k
      );
    }
  }

  public static void main(String[] args) throws Exception {
    KthLargestElementInAnArray kthLargestElementInAnArray = new KthLargestElementInAnArray();
    Params[] testCases = new Params[] {
      new Params(new int[] { 3, 2, 1, 5, 6, 4 }, 2),
      new Params(new int[] { 3, 2, 3, 1, 2, 4, 5, 5, 6 }, 4),
    };
    // NOTE: the method must be public to make .getMethod work
    String[] testMethodNames = new String[] { "findKthLargestQuickSort" };

    for (Params params : testCases) {
      for (String methodName : testMethodNames) {
        java.lang.reflect.Method method = kthLargestElementInAnArray
          .getClass()
          .getMethod(methodName, int[].class, int.class);
        int kthLargest = (int) method.invoke(
          kthLargestElementInAnArray,
          params.nums,
          params.k
        );
        String printContent = String.format(
          "Method Name: %s\nInput: %s, Output: %s",
          methodName,
          params.toString(),
          kthLargest
        );
        System.out.println(printContent);
      }
    }
  }
}

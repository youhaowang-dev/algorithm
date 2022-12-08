// tag: array, divide and conquer, sorting, heap, priority queue, quickselect
// Facebook 28 Amazon 17 Spotify 11 LinkedIn 8 Microsoft 5 Adobe 5 Apple 4 Bloomberg 3 Google 2 Walmart Global Tech 2 Intuit 2
// source: https://leetcode.com/problems/kth-largest-element-in-an-array/description/

// description: Given an integer array nums and an integer k, return the kth largest element in the array.
//              Note that it is the kth largest element in the sorted order, not the kth distinct element.
//              You must solve it in O(n) time complexity.
// example: nums = [3,2,1,5,6,4], k = 2, output = 5
//          nums = [3,2,3,1,2,4,5,5,6], k = 4, output = 4

import java.util.Arrays;
import java.util.Map;

class KthLargestElementInAnArray {

  public int findKthLargestQuickSort(int[] nums, int k) {
    (new QuickSort()).quickSort(nums, 0, nums.length - 1);

    return nums[nums.length - 1 - (k - 1)];
  }

  public int findKthLargestQuickSortV2(int[] nums, int k) {
    (new QuickSort()).quickSortV2(nums, 0, nums.length - 1);

    return nums[nums.length - 1 - (k - 1)];
  }

  static class Params {

    public int[] nums;
    public int k;

    public Params(int[] nums, int k) {
      this.nums = nums;
      this.k = k;
    }

    public String toString() {
      return String.format("nums: %s, k: %s", Arrays.toString(nums), k);
    }
  }

  public static void main(String[] args) throws Exception {
    KthLargestElementInAnArray kthLargestElementInAnArray = new KthLargestElementInAnArray();
    Params[] testCases = new Params[] {
      new Params(new int[] { 3, 2, 1, 5, 6, 4 }, 2),
      new Params(
        new int[] { 1, 1, 1, 1, 11, 11, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 },
        4
      ),
    };
    // NOTE: the method must be public to make .getMethod work
    String[] testMethodNames = new String[] {
      "findKthLargestQuickSort",
      "findKthLargestQuickSortV2",
    };

    for (Params params : testCases) {
      for (String methodName : testMethodNames) {
        System.out.println(
          String.format(
            "Method Name: %s\nInput: %s",
            methodName,
            params.toString()
          )
        );
        java.lang.reflect.Method method = kthLargestElementInAnArray
          .getClass()
          .getMethod(methodName, int[].class, int.class);
        int[] numsCopy = Arrays.copyOf(params.nums, params.nums.length);
        int kthLargest = (int) method.invoke(
          kthLargestElementInAnArray,
          numsCopy,
          params.k
        );
        System.out.println(
          String.format(
            "Output: %s. Input Array: %s",
            kthLargest,
            Arrays.toString(numsCopy)
          )
        );
      }
    }
  }
}

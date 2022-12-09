// tag: array, divide and conquer, sorting, heap, priority queue, quickselect
// Facebook 28 Amazon 17 Spotify 11 LinkedIn 8 Microsoft 5 Adobe 5 Apple 4 Bloomberg 3 Google 2 Walmart Global Tech 2 Intuit 2
// source: https://leetcode.com/problems/kth-largest-element-in-an-array/description/

// description: Given an integer array nums and an integer k, return the kth largest element in the array.
//              Note that it is the kth largest element in the sorted order, not the kth distinct element.
//              You must solve it in O(n) time complexity.
// example: nums = [3,2,1,5,6,4], k = 2, output = 5
//          nums = [3,2,3,1,2,4,5,5,6], k = 4, output = 4

import java.util.*; // write an assumption for this in interview

class KthLargestElementInAnArray {

  public int findKthLargestByQuickSort(int[] nums, int k) {
    (new QuickSort()).quickSort(nums, 0, nums.length - 1);

    return nums[nums.length - 1 - (k - 1)];
  }

  // The idea is to init a heap "the smallest element first", and add all elements
  // from the array into this heap one by one keeping the size of the heap always
  // less or equal to k. That would results in a heap containing k largest elements of the array.
  // The head of this heap is the answer, i.e. the kth largest element of the array.
  public int findKthLargestByHeap(int[] nums, int k) {
    // Comparator maxHeapComparator = new Comparator<Integer>() {
    //   @Override
    //   public int compare(Integer num1, Integer num2) {
    //     return Integer.compare(num1, num2); // for min heap, use (num2, num1)
    //   }
    // };

    // PriorityQueue<Integer> topKNums = new PriorityQueue<Integer>(
    //   maxHeapComparator
    // );

    // Queue<Integer> topKNums = new PriorityQueue<Integer>((num1, num2) -> {
    //   return num1 - num2;
    // });

    Queue<Integer> topKNums = new PriorityQueue<Integer>((num1, num2) ->
      num1 - num2
    );
    for (int num : nums) {
      topKNums.add(num);
      if (topKNums.size() > k) {
        topKNums.poll();
      }
    }

    return topKNums.peek();
  }

  static class Params {

    public int[] nums;
    public int k;

    public Params(int[] nums, int k) {
      this.nums = nums;
      this.k = k;
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
      "findKthLargestByQuickSort",
      "findKthLargestByHeap",
    };

    for (Params params : testCases) {
      for (String methodName : testMethodNames) {
        int[] numsCopy = Arrays.copyOf(params.nums, params.nums.length);
        System.out.println(
          String.format(
            "Method Name: %s\nInput Array: %s, K: %s",
            methodName,
            Arrays.toString(numsCopy),
            params.k
          )
        );
        java.lang.reflect.Method method = kthLargestElementInAnArray
          .getClass()
          .getMethod(methodName, int[].class, int.class);
        int kthLargest = (int) method.invoke(
          kthLargestElementInAnArray,
          numsCopy,
          params.k
        );
        System.out.println(
          String.format(
            "Output: %s\nInput Array: %s",
            kthLargest,
            Arrays.toString(numsCopy)
          )
        );
      }
    }
  }
}

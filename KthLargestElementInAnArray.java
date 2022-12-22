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

  // quick select
  // time complexity: O(n) where partition costs n + n/2 + n/4 + ... +  = 2n
  // The worst case is that partitioning always results in very skewed partition sizes.
  // Consider what would happen if the first partitioning only removed one item. And the second only removed one, etc.
  // The result would be: N + (N-1) + (N-2) ... Which is (n^2 + n)/2), or O(n^2).
  public int findKthLargest(int[] nums, int k) {
    // kth largest index = length - k

    return this.partition(nums, nums.length - k, 0, nums.length - 1);
  }

  private int partition(int[] nums, int targetIndex, int start, int end) {
    if (start >= end) {
      // this means the target partition has been sorted, so the targetIndex will point to the target value
      return nums[targetIndex];
    }

    int left = start;
    int right = end;
    int pivot = nums[(start + end) / 2];
    while (left <= right) {
      while (left <= right && nums[left] < pivot) {
        left++;
      }
      while (left <= right && nums[right] > pivot) {
        right--;
      }
      if (left <= right) {
        this.swap(nums, left, right);
        left++;
        right--;
      }
    }

    // now three partitions can exist and k can be in one of them
    // start - left: unsorted
    // left - right: sorted and pivot in this range; exit condition
    // right - end: unsorted
    if (targetIndex <= right) {
      // sort next partition
      return this.partition(nums, targetIndex, start, right);
    } else {
      // sort next partition
      return this.partition(nums, targetIndex, left, end);
    }
  }

  private void swap(int[] nums, int left, int right) {
    int leftCopy = nums[left];
    nums[left] = nums[right];
    nums[right] = leftCopy;
  }

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

  // use to partition of quick sort
  // since the pivot index is at the sorted position
  // we can compare the index with the index of the kth largest,
  // so we can pick the left or right to continue the partition and find the partition_index==kthlargest_index
  // time complexity: O(n) where partition costs n + n/2 + n/4 + ... +  = 2n

  // space complexity: log(n) stack space
  public int findKthLargestByQuickSelect(int[] nums, int k) {
    if (nums.length < k) {
      return Integer.MIN_VALUE;
    }

    // if the array is sorted, the kth largest value index is known
    int kthLargestIndex = nums.length - 1 - (k - 1);

    return this.quickSelect(nums, 0, nums.length - 1, kthLargestIndex);
  }

  private int quickSelect(
    int[] nums,
    int partitionStart,
    int partitionEnd,
    int kthLargestIndex
  ) {
    int pivotIndex = this.partition(nums, partitionStart, partitionEnd);

    if (kthLargestIndex == pivotIndex) {
      // found
      return nums[kthLargestIndex];
    }
    if (kthLargestIndex > pivotIndex) {
      // search in the right partition
      return quickSelect(nums, pivotIndex + 1, partitionEnd, kthLargestIndex);
    }
    if (kthLargestIndex < pivotIndex) {
      // search in the left partition
      return quickSelect(nums, partitionStart, pivotIndex - 1, kthLargestIndex);
    }

    return Integer.MIN_VALUE;
  }

  private int partition(int[] nums, int partitionStart, int partitionEnd) {
    int pivot = nums[partitionEnd];
    int partitionIndex = partitionStart;
    for (int index = partitionStart; index < partitionEnd; index++) {
      if (nums[index] <= pivot) {
        this.swap(nums, index, partitionIndex);
        partitionIndex++;
      }
    }
    // start to end-1 are processed, now process the end
    this.swap(nums, partitionIndex, partitionEnd);

    return partitionIndex;
  }

  private void swap(int[] nums, int lowIndex, int highIndex) {
    int lowCopy = nums[lowIndex];
    nums[lowIndex] = nums[highIndex];
    nums[highIndex] = lowCopy;
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
      "findKthLargestByQuickSelect",
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

// Array, Binary Search, Divide and Conquer, Binary Indexed Tree, Segment Tree, Merge Sort, Ordered Set
// Google 5 Apple 3 Amazon 3 Microsoft 3 Adobe 2 Bloomberg 2 Infosys 2 Uber 4 Myntra 3 Walmart Global Tech 2 Sprinklr 2
// https://leetcode.com/problems/count-of-smaller-numbers-after-self/

// Given an integer array nums, return an integer array counts where counts[i] is the number of smaller elements to the right of nums[i].

// Example 1:
// Input: nums = [5,2,6,1]
// Output: [2,1,1,0]
// Explanation:
// To the right of 5 there are 2 smaller elements (2 and 1).
// To the right of 2 there is only 1 smaller element (1).
// To the right of 6 there is 1 smaller element (1).
// To the right of 1 there is 0 smaller element.

// Example 2:
// Input: nums = [-1]
// Output: [0]

// Example 3:
// Input: nums = [-1,-1]
// Output: [0,0]
import java.util.*;

final class CountOfSmallerNumbersAfterSelf {

  public List<Integer> countSmaller(int[] nums) {
    int[] numsSorted = nums.clone();
    System.out.println("before sorting " + Arrays.toString(numsSorted));
    this.mergesort(numsSorted, 0, nums.length - 1);
    System.out.println(
      "Arrays.toString(numsSorted): " + Arrays.toString(numsSorted)
    );

    List<Integer> counts = new ArrayList<>();

    return counts;
  }

  private void mergesort(int[] nums, int left, int right) {
    // exit condition
    if (left >= right) {
      return;
    }

    int mid = left - (left - right) / 2;
    // mergesort left and right
    this.mergesort(nums, left, mid);
    this.mergesort(nums, mid + 1, right);
    // merge left and right
    this.merge(nums, left, mid, right);
  }

  // left [left, mid]
  // right [mid + 1, right]
  private void merge(int[] nums, int left, int mid, int right) {
    int[] leftArray = Arrays.copyOfRange(nums, left, mid + 1);
    int[] rightArray = Arrays.copyOfRange(nums, mid + 1, right + 1);
    int leftSize = leftArray.length;
    int rightSize = rightArray.length;
    int leftIndex = 0;
    int rightIndex = 0;
    int mergeIndex = left;
    while (leftIndex < leftSize && rightIndex < rightSize) {
      if (leftArray[leftIndex] < rightArray[rightIndex]) {
        nums[mergeIndex] = leftArray[leftIndex];
        leftIndex++;
      } else {
        nums[mergeIndex] = rightArray[rightIndex];
        rightIndex++;
      }
      mergeIndex++;
    }
    while (leftIndex < leftSize) {
      nums[mergeIndex] = leftArray[leftIndex];
      leftIndex++;
      mergeIndex++;
    }
    while (rightIndex < rightSize) {
      nums[mergeIndex] = rightArray[rightIndex];
      rightIndex++;
      mergeIndex++;
    }
  }

  class ArrayIterator {

    int[] nums;
    int start;
    int end;

    public ArrayIterator(int[] nums, int start, int end) {
      this.nums = nums;
      this.start = start;
      this.end = end;
    }

    public boolean hasNext() {
      return start <= end;
    }

    public int popNext() {
      int currentVal = nums[start];
      start++;
      return currentVal;
    }

    public int getNext() {
      return nums[start];
    }
  }

  private void quickSort(int[] nums, int first, int last) {
    if (first >= last) {
      return;
    }
    int partitionIndex = this.partition(nums, first, last);
    this.quickSort(nums, first, partitionIndex - 1);
    this.quickSort(nums, partitionIndex, last);
  }

  private int partition(int[] nums, int first, int last) {
    int partitionIndex = 0;
    int pivotValue = nums[last];
    for (int index = 0; index < last; index++) {
      if (nums[index] <= pivotValue) {
        this.swap(nums, index, partitionIndex);
        partitionIndex++;
      }
    }
    swap(nums, partitionIndex, last);

    return partitionIndex;
  }

  private void swap(int[] nums, int index1, int index2) {
    int index1Copy = nums[index1];
    nums[index1] = nums[index2];
    nums[index2] = index1Copy;
  }

  public static void main(String[] args) throws Exception {
    CountOfSmallerNumbersAfterSelf CountOfSmallerNumbersAfterSelf = new CountOfSmallerNumbersAfterSelf();
    int[][] testCases = new int[][] {
      { 5, 2, 6, 1 },
      // , { -1 }, { -1, -1 }
    };
    // NOTE: the method must be public to make .getMethod work
    String[] testMethodNames = new String[] { "countSmaller" };

    for (int[] nums : testCases) {
      for (String methodName : testMethodNames) {
        java.lang.reflect.Method method = CountOfSmallerNumbersAfterSelf
          .getClass()
          .getMethod(methodName, int[].class);
        ArrayList<Integer> counts = (ArrayList<Integer>) method.invoke(
          CountOfSmallerNumbersAfterSelf,
          nums
        );

        System.out.println("methodName: " + methodName);
        System.out.println("nums: " + Arrays.toString(nums));
        System.out.println("counts: " + Arrays.toString(counts.toArray()));
      }
    }
  }
}

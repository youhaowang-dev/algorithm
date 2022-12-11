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

  // https://leetcode.com/problems/count-of-smaller-numbers-after-self/solutions/445769/merge-sort-clear-simple-explanation-with-examples-o-n-lg-n/
  public List<Integer> countSmallerMergeSort(int[] nums) {
    ValWithIndex[] numsCopy = new ValWithIndex[nums.length];
    for (int i = 0; i < nums.length; i++) {
      numsCopy[i] = new ValWithIndex(nums[i], i);
    }

    int[] counts = new int[nums.length];
    this.mergesort(numsCopy, 0, nums.length - 1, counts);
    List<Integer> countList = new ArrayList<>();
    for (int count : counts) {
      countList.add(count);
    }
    return countList;
  }

  private void mergesort(
    ValWithIndex[] nums,
    int left,
    int right,
    int[] counts
  ) {
    // exit condition
    if (left >= right) {
      return;
    }

    int mid = left - (left - right) / 2;
    // mergesort left and right
    this.mergesort(nums, left, mid, counts);
    this.mergesort(nums, mid + 1, right, counts);
    // merge left and right
    this.merge(nums, left, mid, right, counts);
  }

  // left subarray [left, mid]
  // right subarray [mid + 1, right]
  private void merge(
    ValWithIndex[] nums,
    int left,
    int mid,
    int right,
    int[] counts
  ) {
    SubarrayIterator leftIterator = new SubarrayIterator(nums, left, mid);
    SubarrayIterator rightIterator = new SubarrayIterator(nums, mid + 1, right);
    int mergeIndex = left;
    int numElemsRightArrayLessThanLeftArray = 0;
    while (leftIterator.hasNext() && rightIterator.hasNext()) {
      if (leftIterator.getNext().val <= rightIterator.getNext().val) {
        counts[leftIterator.getNext().originalIndex] +=
          numElemsRightArrayLessThanLeftArray;

        nums[mergeIndex] = leftIterator.popNext();
      } else {
        numElemsRightArrayLessThanLeftArray++;

        nums[mergeIndex] = rightIterator.popNext();
      }
      mergeIndex++;
    }
    while (leftIterator.hasNext()) {
      counts[leftIterator.getNext().originalIndex] +=
        numElemsRightArrayLessThanLeftArray;

      nums[mergeIndex] = leftIterator.popNext();
      mergeIndex++;
    }
    while (rightIterator.hasNext()) {
      nums[mergeIndex] = rightIterator.popNext();
      mergeIndex++;
    }
  }

  class ValWithIndex {

    int val;
    int originalIndex;

    public ValWithIndex(int val, int originalIndex) {
      this.val = val;
      this.originalIndex = originalIndex;
    }
  }

  class SubarrayIterator {

    ValWithIndex[] nums;
    int index;

    public SubarrayIterator(ValWithIndex[] nums, int start, int end) {
      this.index = 0;
      this.nums = Arrays.copyOfRange(nums, start, end + 1);
    }

    public boolean hasNext() {
      return index < nums.length;
    }

    public ValWithIndex popNext() {
      ValWithIndex currentVal = nums[index];
      index++;
      return currentVal;
    }

    public ValWithIndex getNext() {
      return nums[index];
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
    int[][] testCases = new int[][] { { 5, 2, 6, 1 }, { -1 }, { -1, -1 } };
    // NOTE: the method must be public to make .getMethod work
    String[] testMethodNames = new String[] { "countSmallerMergeSort" };

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

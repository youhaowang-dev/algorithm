// tag: Array, Divide and Conquer
import java.util.Arrays;

public final class QuickSort {

  // time complexity: O(nlog(n)) on average, O(n^2) the worst case
  // do O(n) linear scan in log(n) partitions
  // space complexity: O(log(n)) stack space cost where the recursion tree height is log(n)
  public void quickSort(int[] nums, int partitionStart, int partitionEnd) {
    if (partitionStart >= partitionEnd) {
      return; // handle edge cases and exiting condition
    }
    int pivotIndex = this.partition(nums, partitionStart, partitionEnd);
    this.quickSort(nums, partitionStart, pivotIndex - 1);
    this.quickSort(nums, pivotIndex, partitionEnd);
  }

  // Goal: put the pivot value to the sorted position and make sure (left values) <= pivot < (right values)
  // pick a pivot and the pivot index
  // partition index starts at start and moves towards right; all elements at or before the partition index
  // scan from start and swap with partition index value when the current value is greater than pivot
  // set the pivot at the partition index, which is a sorted index
  // return the partition index
  private int partition(int[] nums, int start, int end) {
    int partitionIndex = start; // aka swap to location for the bigger number
    int pivot = nums[end]; // end is picked as the pivot index

    // two pointers moving to right where the index normally moves a little faster
    for (int index = start; index < end; index++) {
      // to move partionIndex to right, all the values to the left must be smaller or equal to pivot
      if (nums[index] <= pivot) {
        this.swap(nums, index, partitionIndex);
        partitionIndex++;
      }
    }
    // the partitionIndex now stops at the sorted position for the pivot value, so swap it with pivot
    this.swap(nums, partitionIndex, end);

    return partitionIndex;
  }

  private void swap(int[] nums, int lowNumIndex, int highNumIndex) {
    int smallerNumberCopy = nums[lowNumIndex];
    nums[lowNumIndex] = nums[highNumIndex];
    nums[highNumIndex] = smallerNumberCopy;
  }

  public static void main(String[] args) throws Exception {
    QuickSort quickSort = new QuickSort();
    int[][] testCases = {
      new int[] { 3, 2, 1, 5, 6, 4 },
      new int[] { 89, 47, 2, 17, 8, 19 },
      new int[] { 1, 1, 1, 1, 11, 11, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 },
      new int[] { 1, 4, 2, 4, 2, 4, 1, 2, 4, 1, 2, 2, 2, 2, 4, 1, 4, 4, 4 },
    };

    String[] testMethodNames = new String[] { "quickSort" };

    for (int[] testCase : testCases) {
      for (String methodName : testMethodNames) {
        int[] numsCopy = Arrays.copyOf(testCase, testCase.length);
        System.out.println(
          String.format(
            "Method Name: %s\nInput: %s",
            methodName,
            Arrays.toString(numsCopy)
          )
        );
        java.lang.reflect.Method method = quickSort
          .getClass()
          .getMethod(methodName, int[].class, int.class, int.class);
        method.invoke(quickSort, numsCopy, 0, numsCopy.length - 1);
        System.out.println(
          String.format("Output: %s", Arrays.toString(numsCopy))
        );
      }
    }
  }
}

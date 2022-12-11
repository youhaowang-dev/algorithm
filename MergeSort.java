import java.util.*;

final class MergeSort {

  // https://www.geeksforgeeks.org/merge-sort/
  // Main function that sorts nums[l..r] using
  public void mergesort(int nums[], int left, int right) {
    if (left < right) {
      // Find the middle point
      int mid = left + (right - left) / 2;

      // Sort first and second halves
      mergesort(nums, left, mid);
      mergesort(nums, mid + 1, right);

      // Merge the sorted halves
      merge(nums, left, mid, right);
    }
  }

  // Merges two subarrays of nums[].
  // First subarray is nums[left..mid]
  // Second subarray is nums[left+1..right]
  public void merge(int nums[], int left, int mid, int right) {
    // int leftArraySize = mid - (left - 1);
    // int rightArraySize = right - (mid + 1 - 1);
    // int[] leftArray = new int[leftArraySize];
    // int[] rightArray = new int[rightArraySize];
    // for (int i = 0; i < leftArraySize; i++) {
    //   leftArray[i] = nums[left + i];
    // }
    // for (int i = 0; i < rightArraySize; i++) {
    //   rightArray[i] = nums[mid + 1 + i];
    // }

    // public static short[] copyOfRange(short[] original, int from, int to)
    // Parameters
    // original − This is the array from which a range is to to be copied.
    // from − This is the initial index of the range to be copied, inclusive.
    // to − This is the final index of the range to be copied, exclusive.
    int[] leftArray = Arrays.copyOfRange(nums, left, mid + 1);
    int[] rightArray = Arrays.copyOfRange(nums, mid + 1, right + 1);
    int leftArraySize = leftArray.length;
    int rightArraySize = rightArray.length;

    // Initial indexes of first and second subarrays
    int leftArrayIndex = 0;
    int rightArrayIndex = 0;
    // Initial index of merged subarray array
    int mergeIndex = left;
    while (leftArrayIndex < leftArraySize && rightArrayIndex < rightArraySize) {
      if (leftArray[leftArrayIndex] <= rightArray[rightArrayIndex]) {
        nums[mergeIndex] = leftArray[leftArrayIndex];
        leftArrayIndex++;
      } else {
        nums[mergeIndex] = rightArray[rightArrayIndex];
        rightArrayIndex++;
      }
      mergeIndex++;
    }

    /* Copy remaining elements of leftArray[] if any */
    while (leftArrayIndex < leftArraySize) {
      nums[mergeIndex] = leftArray[leftArrayIndex];
      leftArrayIndex++;
      mergeIndex++;
    }

    /* Copy remaining elements of rightArray[] if any */
    while (rightArrayIndex < rightArraySize) {
      nums[mergeIndex] = rightArray[rightArrayIndex];
      rightArrayIndex++;
      mergeIndex++;
    }
  }

  public static void main(String[] args) throws Exception {
    MergeSort MergeSort = new MergeSort();
    int[][] testCases = {
      new int[] { 3, 2, 1, 5, 6, 4 },
      new int[] { 89, 47, 2, 17, 8, 19 },
      new int[] { 1, 1, 1, 1, 11, 11, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 },
      new int[] { 1, 4, 2, 4, 2, 4, 1, 2, 4, 1, 2, 2, 2, 2, 4, 1, 4, 4, 4 },
    };

    String[] testMethodNames = new String[] { "mergesort" };

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
        java.lang.reflect.Method method = MergeSort
          .getClass()
          .getMethod(methodName, int[].class, int.class, int.class);
        method.invoke(MergeSort, numsCopy, 0, numsCopy.length - 1);
        System.out.println(
          String.format("Output: %s", Arrays.toString(numsCopy))
        );
      }
    }
  }
}

import java.util.Arrays;

public final class QuickSort {

  // time complexity: O(nlog(n)) on average, O(n^2) the worst case
  // space complexity: O(stack space)
  public void quickSort(int[] nums, int left_start, int right_start) {
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

    // now left == right, so the pivot value should be at this position
    int pivot_index = left;
    // swap it with the pivot value
    nums[left_start] = nums[pivot_index];
    nums[pivot_index] = pivot;

    // continue unsorted partitions, pivot_index is already at the sorted position
    this.quickSort(nums, left_start, pivot_index - 1);
    this.quickSort(nums, pivot_index + 1, right_start);
  }

  public void quickSortV2(int[] nums, int left_start, int right_start) {
    int pivotIndex = this.setPivot(nums, left_start, right_start);
    if (left_start < pivotIndex - 1) {
      this.quickSortV2(nums, left_start, pivotIndex - 1);
    }
    if (right_start > pivotIndex) {
      this.quickSortV2(nums, pivotIndex, right_start);
    }
  }

  // set the pivot at the sorted position and return the pivot index
  private int setPivot(int[] nums, int left_start, int right_start) {
    int left = left_start;
    int right = right_start;
    int pivot = nums[left_start];

    while (left <= right) {
      while (nums[left] < pivot) {
        left++;
      }
      while (nums[right] > pivot) {
        right--;
      }
      if (left <= right) {
        int left_copy = nums[left];
        nums[left] = nums[right];
        nums[right] = left_copy;
        // move pointers after swapping
        left++;
        right--;
      }
    }

    return left; // left = right = pivot index
  }

  public static void main(String[] args) throws Exception {
    QuickSort quickSort = new QuickSort();
    int[][] testCases = {
      new int[] { 3, 2, 1, 5, 6, 4 },
      new int[] { 1, 1, 1, 1, 11, 11, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 },
      new int[] { 1, 4, 2, 4, 2, 4, 1, 2, 4, 1, 2, 2, 2, 2, 4, 1, 4, 4, 4 },
    };

    String[] testMethodNames = new String[] { "quickSort", "quickSortV2" };

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

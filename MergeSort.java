import java.util.*;

final class MergeSort {

  // https://www.geeksforgeeks.org/merge-sort/
  // Main function that sorts arr[l..r] using
  public void mergesort(int arr[], int l, int r) {
    if (l < r) {
      // Find the middle point
      int m = l + (r - l) / 2;

      // Sort first and second halves
      mergesort(arr, l, m);
      mergesort(arr, m + 1, r);

      // Merge the sorted halves
      merge(arr, l, m, r);
    }
  }

  // Merges two subarrays of arr[].
  // First subarray is arr[l..m]
  // Second subarray is arr[m+1..r]
  public void merge(int arr[], int l, int m, int r) {
    // Find sizes of two subarrays to be merged
    int n1 = m - l + 1;
    int n2 = r - m;

    /* Create temp arrays */
    int L[] = new int[n1];
    int R[] = new int[n2];

    /*Copy data to temp arrays*/
    for (int i = 0; i < n1; ++i) L[i] = arr[l + i];
    for (int j = 0; j < n2; ++j) R[j] = arr[m + 1 + j];

    /* Merge the temp arrays */

    // Initial indexes of first and second subarrays
    int i = 0, j = 0;

    // Initial index of merged subarray array
    int k = l;
    while (i < n1 && j < n2) {
      if (L[i] <= R[j]) {
        arr[k] = L[i];
        i++;
      } else {
        arr[k] = R[j];
        j++;
      }
      k++;
    }

    /* Copy remaining elements of L[] if any */
    while (i < n1) {
      arr[k] = L[i];
      i++;
      k++;
    }

    /* Copy remaining elements of R[] if any */
    while (j < n2) {
      arr[k] = R[j];
      j++;
      k++;
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

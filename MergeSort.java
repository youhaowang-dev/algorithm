import java.util.*;

final class MergeSort {

  public void mergesort(int[] nums, int first, int last) {}

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

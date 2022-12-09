// tag: Array, Binary Search
// Apple 9 Google 4 Amazon 4 Microsoft 4 Adobe 3 Yahoo 2
// source: https://leetcode.com/problems/search-insert-position/description/
// description: Given a sorted array of distinct integers and a target value,
//              return the index if the target is found. If not, return the index where it would be if it were inserted in order.
//              You must write an algorithm with O(log n) runtime complexity.
// example: Input: nums = [1,3,5,6], target = 5, Output: 2
//          Input: nums = [1,3,5,6], target = 2, Output: 1
//          Input: nums = [1,3,5,6], target = 7, Output: 4

final class SearchInsertPosition {

  public static void main(String[] args) throws Exception {
    SearchInsertPosition SearchInsertPosition = new SearchInsertPosition();
    int[] nums = new int[] { 1, 3, 5, 6 };
    int[] testCases = new int[] { 2, 5, 7 };
    // NOTE: the method must be public to make .getMethod work
    String[] testMethodNames = new String[] {};

    for (int target : testCases) {
      for (String methodName : testMethodNames) {
        java.lang.reflect.Method method = SearchInsertPosition
          .getClass()
          .getMethod(methodName, int[].class, int.class);
        int insertIndex = (int) method.invoke(
          SearchInsertPosition,
          nums,
          target
        );

        System.out.println(
          String.format(
            "Method Name: %s\nInput: %s, Output: %s",
            methodName,
            java.util.Arrays.toString(nums) + " target: " + target,
            insertIndex
          )
        );
      }
    }
  }
}

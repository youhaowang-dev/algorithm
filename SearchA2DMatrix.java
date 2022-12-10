// tag: Array, Binary Search, Matrix
// Amazon 17 Apple 8 Bloomberg 5 Microsoft 3 Google 3 Adobe 3 Visa 2 Walmart Global Tech 2
// source: https://leetcode.com/problems/search-a-2d-matrix/
// description: Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:
//              Integers in each row are sorted from left to right.
//              The first integer of each row is greater than the last integer of the previous row.
// Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3, Output: true
// Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13, Output: false

final class SearchA2DMatrix {

  // given the matrix properties
  // binary search can be used on the sorted array
  // need to take care of 1D => 2D conversion
  public boolean searchMatrix(int[][] matrix, int target) {
    return false;
  }

  // get matrix value by using 1D index
  private int getValue(int[][] matrix, int index) {
    return -1;
  }

  public static void main(String[] args) throws Exception {
    SearchA2DMatrix SearchA2DMatrix = new SearchA2DMatrix();
    int[] targets = new int[] { 1, 11, 60, 0 };
    int[][] matrix = new int[][] {
      { 1, 3, 5, 7 },
      { 10, 11, 16, 20 },
      { 23, 30, 34, 60 },
    };
    // NOTE: the method must be public to make .getMethod work
    String[] testMethodNames = new String[] { "searchMatrix" };

    for (int target : targets) {
      for (String methodName : testMethodNames) {
        java.lang.reflect.Method method = SearchA2DMatrix
          .getClass()
          .getMethod(methodName, int[][].class, int.class);
        boolean found = (boolean) method.invoke(
          SearchA2DMatrix,
          matrix,
          target
        );

        System.out.println(
          String.format(
            "Method Name: %s\nInput: %s, Output: %s",
            methodName,
            java.util.Arrays.deepToString(matrix) + " Target: " + target,
            found
          )
        );
      }
    }
  }
}

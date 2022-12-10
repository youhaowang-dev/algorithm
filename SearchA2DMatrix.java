// tag: Array, Binary Search, Matrix
// Amazon 17 Apple 8 Bloomberg 5 Microsoft 3 Google 3 Adobe 3 Visa 2 Walmart Global Tech 2
// source: https://leetcode.com/problems/search-a-2d-matrix/
// description: Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:
//              Integers in each row are sorted from left to right.
//              The first integer of each row is greater than the last integer of the previous row.
// Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3, Output: true
// Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13, Output: false
import java.util.*;

final class SearchA2DMatrix {

  // given the matrix properties
  // binary search can be used on the sorted array
  // need to take care of 1D => 2D conversion
  public boolean searchMatrix(int[][] matrix, int target) {
    if (matrix.length == 0 || matrix[0].length == 0) {
      return false;
    }
    int start = 0;
    int end = matrix.length * matrix[0].length - 1;
    while (start + 1 < end) {
      int mid = start - (start - end) / 2;
      int midVal = this.getValue(matrix, mid);
      if (midVal == target) {
        return true;
      }
      if (midVal < target) {
        start = mid;
      }
      if (midVal > target) {
        end = mid;
      }
      // System.out.println(
      //   Arrays.toString(
      //     new Object[] {
      //       "target: " + target,
      //       "mid: " + mid,
      //       "midVal: " + midVal,
      //       "start: " + start,
      //       "end: " + end,
      //     }
      //   )
      // );
    }

    if (this.getValue(matrix, start) == target) {
      return true;
    }
    if (this.getValue(matrix, end) == target) {
      return true;
    }

    return false;
  }

  // get matrix value by using 1D index
  // given [[1,2,3],[4,5,6],[7,8,9]]
  // index = 3 => rowIndex = 1, columnIndex = 0 => rowIndex = index / columnCount = 3/3 = 1, columnIndex = index % columnCount = 3%3=0
  // index = 5 => expect value = 6, expect rowIndex = 1 = 5 / 3, columnIndex = 2 = 5 % 3
  private int getValue(int[][] matrix, int index) {
    if (
      matrix.length == 0 ||
      matrix[0].length == 0 ||
      index < 0 ||
      index > matrix.length * matrix[0].length
    ) {
      return Integer.MAX_VALUE;
    }

    int columnCount = matrix[0].length;
    int rowIndex = index / columnCount;
    int columnIndex = index % columnCount;

    return matrix[rowIndex][columnIndex];
  }

  public static void main(String[] args) throws Exception {
    SearchA2DMatrix SearchA2DMatrix = new SearchA2DMatrix();
    int[] targets = new int[] { 1, 3, 5, 7, 10, 20, 23, 60, 0, 22 };
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
            Arrays.deepToString(matrix) + " Target: " + target,
            found
          )
        );
      }
    }
  }
}

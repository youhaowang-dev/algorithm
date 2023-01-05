// Array, Binary Search, Matrix
// Amazon 17 Apple 8 Bloomberg 5 Microsoft 3 Google 3 Adobe 3 Visa 2 Walmart Global Tech 2
// https://leetcode.com/problems/search-a-2d-matrix/
// Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:
//              Integers in each row are sorted from left to right.
//              The first integer of each row is greater than the last integer of the previous row.
// Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3, Output: true
// Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13, Output: false
import java.util.*;

final class SearchA2DMatrix {

  // brute force linear search each row and its cols
  // time O(rowCount * colCount)

  // binary search time O(log(rowCount * colCount))
  // given the matrix properties
  // binary search can be used on the sorted array
  // need to take care of 1D => 2D conversion
  public boolean searchMatrix(int[][] matrix, int target) {
    if (matrix.length == 0 || matrix[0].length == 0) {
      return false;
    }
    int totalLength = matrix.length * matrix[0].length;
    int left = 0;
    int right = totalLength - 1;
    while (left + 1 < right) {
      int mid = left - (left - right) / 2;
      int midVal = this.getVal(matrix, mid);
      if (midVal == target) {
        return true;
      }
      if (midVal < target) {
        left = mid;
      }
      if (midVal > target) {
        right = mid;
      }
    }

    // left == right or left+1 == right
    if (this.getVal(matrix, left) == target) {
      return true;
    }
    if (this.getVal(matrix, right) == target) {
      return true;
    }

    return false;
  }

  // get matrix value by using 1D index
  // given [[1,2,3],[4,5,6],[7,8,9]]
  // index = 3 => rowIndex = 1, colIndex = 0 => rowIndex = index / colCount = 3/3 = 1, colIndex = index % colCount = 3%3=0
  // index = 5 => expect value = 6, expect rowIndex = 1 = 5 / 3, colIndex = 2 = 5 % 3
  private int getVal(int[][] matrix, int index) {
    if (
      matrix.length == 0 ||
      matrix[0].length == 0 ||
      index < 0 ||
      index > matrix.length * matrix[0].length
    ) {
      return Integer.MAX_VALUE;
    }

    int colCount = matrix[0].length;
    int rowIndex = index / colCount;
    int colIndex = index % colCount;

    return matrix[rowIndex][colIndex];
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

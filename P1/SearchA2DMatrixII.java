// Array, Binary Search, Divide and Conquer, Matrix
// Amazon 6 Microsoft 5 Bloomberg 3 Adobe 3 Zillow 2 Apple 3 Oracle 3 Google 2 PayTM 2 Facebook 7 ByteDance 7 Goldman Sachs 3 Paypal 2 Salesforce 2 Uber 2 Nvidia 2
// https://leetcode.com/problems/search-a-2d-matrix-ii/
// Write an efficient algorithm that searches for a val target in an m x n integer matrix matrix. This matrix has the following properties:
//              Integers in each row are sorted in ascending from left to right.
//              Integers in each column are sorted in ascending from top to bottom.
// Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5, Output: true
// Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20, Output: false
import java.util.*;

final class SearchA2DMatrixII {

  // Because the rows and columns of the matrix are sorted (from left-to-right and top-to-bottom, respectively),
  // we can prune O(m) or O(n) elements when looking at any particular val.

  // pick top-right or the bottom-left corner as the "middle" vals
  // move rowIndex and colIndex based on comparision
  // O(rowCount + columnCount)
  // https://leetcode.com/problems/search-a-2d-matrix-ii/solutions/127690/search-a-2d-matrix-ii/
  // This would work equally well with a pointer initialized to the top-right.
  // Neither of the other two corners would work, as pruning a row/column might prevent us from achieving the correct answer.
  public boolean searchMatrix(int[][] matrix, int target) {
    if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
      return false;
    }

    // start position at bottom left corner, can only go up or go right
    int rowIndex = matrix.length - 1; // move up to become smaller
    int colIndex = 0; // move right to become larger
    // >= <= because we still need to search in the first row or the last column
    while (rowIndex >= 0 && colIndex <= matrix[0].length - 1) {
      int val = matrix[rowIndex][colIndex];
      if (val == target) {
        return true;
      }
      if (val > target) {
        // skip the row as all vals of the row right side are greater than target
        rowIndex--;
      }
      if (val < target) {
        // check within the current row
        colIndex++;
      }
    }
    return false;
  }

  public static void main(String[] args) throws Exception {
    SearchA2DMatrixII SearchA2DMatrixII = new SearchA2DMatrixII();
    int[] targets = new int[] { 1, 4, 7, 11, 15, 10, 24, 20, 0 };
    int[][] matrix = new int[][] {
      { 1, 4, 7, 11, 15 },
      { 2, 5, 8, 12, 19 },
      { 3, 6, 9, 16, 22 },
      { 10, 13, 14, 17, 24 },
      { 18, 21, 23, 26, 30 },
    };
    // NOTE: the method must be public to make .getMethod work
    String[] testMethodNames = new String[] { "searchMatrix" };

    for (int target : targets) {
      for (String methodName : testMethodNames) {
        java.lang.reflect.Method method = SearchA2DMatrixII
          .getClass()
          .getMethod(methodName, int[][].class, int.class);
        boolean found = (boolean) method.invoke(
          SearchA2DMatrixII,
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

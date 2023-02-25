// Array, Dynamic Programming
// Amazon 3 DE Shaw 2 Apple 5 Microsoft 2 Google 4 Adobe 3 Bloomberg 3

// Given a triangle array, return the minimum path sum from top to bottom.
// For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

// https://leetcode.com/problems/triangle/description/

// Example 1:

// Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
// Output: 11
// Explanation: The triangle looks like:
//    2
//   3 4
//  6 5 7
// 4 1 8 3
// The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
// Example 2:

// Input: triangle = [[-10]]
// Output: -10

class Triangle {

  // dp
  // state: the min path sum from 0,0 to row,col
  public int minimumTotal(List<List<Integer>> triangle) {
    int rowCount = triangle.size();
    int colCount = triangle.size(); // this is the input triangle criteria  // triangle.get(triangle.size() - 1).size();
    int[][] minPathSums = new int[rowCount][colCount];
    minPathSums[0][0] = triangle.get(0).get(0);

    // init first and last of each row as they dont need to sum with others
    for (int i = 1; i < rowCount; i++) {
      int prevSumRow = i - 1;
      int prevLeftmostSumCol = 0;
      int prevRightmostSumCol = i - 1;
      minPathSums[i][0] =
        triangle.get(i).get(0) + minPathSums[prevSumRow][prevLeftmostSumCol];
      minPathSums[i][i] =
        triangle.get(i).get(i) + minPathSums[prevSumRow][prevRightmostSumCol];
    }

    for (int row = 1; row < rowCount; row++) {
      for (int col = 1; col < row; col++) { // col < row is for the triangle boundary
        // current = min(prev1, prev2) + triangle val
        int prevRow = row - 1;
        int prevCol1 = col;
        int prevCol2 = col - 1;
        int prevMinSum = Math.min(
          minPathSums[prevRow][prevCol1],
          minPathSums[prevRow][prevCol2]
        );
        minPathSums[row][col] = triangle.get(row).get(col) + prevMinSum;
      }
    }

    int minPathSum = Integer.MAX_VALUE;
    // find the min sum in the last row
    for (int num : minPathSums[rowCount - 1]) {
      minPathSum = Math.min(minPathSum, num);
    }

    return minPathSum;
  }

  // divide and conquer with memoization
  // The memoization table ensures that minPath is only called once for each cell. As there are n^2 cells, we get a total time complexity of O(n^2)).
  public int minimumTotal(List<List<Integer>> triangle) {
    Map<Integer, Integer> indexHashToSum = new HashMap<>();
    return this.findMinSumMemoized(triangle, 0, 0, indexHashToSum);
  }

  private int findMinSumMemoized(
    List<List<Integer>> triangle,
    int row,
    int col,
    Map<Integer, Integer> indexHashToSum
  ) {
    if (row == triangle.size()) {
      return 0;
    }

    int indexHash = this.getIndexHash(row, col, triangle);

    if (indexHashToSum.containsKey(indexHash)) {
      return indexHashToSum.get(indexHash);
    }

    int minSum =
      (
        triangle.get(row).get(col) +
        Math.min(
          this.findMinSumMemoized(triangle, row + 1, col, indexHashToSum),
          this.findMinSumMemoized(triangle, row + 1, col + 1, indexHashToSum)
        )
      );

    indexHashToSum.put(indexHash, minSum);

    return minSum;
  }

  private int getIndexHash(int row, int col, List<List<Integer>> triangle) {
    int lastRowLength = triangle.get(triangle.size() - 1).size();

    return row + col * lastRowLength;
  }

  // divide and conquer
  public int minimumTotal(List<List<Integer>> triangle) {
    return this.findMinSum(triangle, 0, 0);
  }

  private int findMinSum(List<List<Integer>> triangle, int row, int col) {
    if (row == triangle.size()) {
      return 0;
    }

    return (
      triangle.get(row).get(col) +
      Math.min(
        this.findMinSum(triangle, row + 1, col),
        this.findMinSum(triangle, row + 1, col + 1)
      )
    );
  }

  // traversal
  public int minimumTotal(List<List<Integer>> triangle) {
    return this.traverse(triangle, 0, 0, 0);
  }

  private int traverse(
    List<List<Integer>> triangle,
    int row,
    int col,
    int sum
  ) {
    if (row == triangle.size()) {
      // out of bound
      return sum;
    }

    int nextSum = sum + triangle.get(row).get(col);

    return Math.min(
      this.traverse(triangle, row + 1, col, nextSum),
      this.traverse(triangle, row + 1, col + 1, nextSum)
    );
  }
}

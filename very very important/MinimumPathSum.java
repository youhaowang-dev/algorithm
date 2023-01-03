// Array, Dynamic Programming, Matrix
// Amazon 6 Google 4 Bloomberg 4 Microsoft 2 Goldman Sachs 2 AQR Capital Management LLC 2 Uber 5 Oracle 3 Square 3 Apple 2 Snapchat 2 ByteDance 2 Tesla 3 Adobe 2 Paypal 2 ServiceNow 2
// https://leetcode.com/problems/minimum-path-sum/

// Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
// Note: You can only move either down or right at any point in time.

// Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
// Output: 7
// Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

class MinimumPathSum {

  // dp
  // state: minPathSums[row][col] is the min path sum from 0,0 to row,col
  // minPathSums[row, col] = grid[row, col] + min(minPathSums[row - 1, col], minPathSums[row, col - 1])
  public int minPathSum(int[][] grid) {
    if (
      grid == null || grid.length == 0 || grid[0] == null || grid[0].length == 0
    ) {
      return 0;
    }

    int rowCount = grid.length;
    int colCount = grid[0].length;
    int[][] minPathSums = new int[rowCount][colCount];
    minPathSums[0][0] = grid[0][0];
    for (int row = 1; row < rowCount; row++) {
      minPathSums[row][0] = grid[row][0] + minPathSums[row - 1][0];
    }
    for (int col = 1; col < colCount; col++) {
      minPathSums[0][col] = grid[0][col] + minPathSums[0][col - 1];
    }

    for (int row = 1; row < rowCount; row++) {
      for (int col = 1; col < colCount; col++) {
        int prevMinPathSum = Math.min(
          minPathSums[row - 1][col],
          minPathSums[row][col - 1]
        );
        minPathSums[row][col] = grid[row][col] + prevMinPathSum;
      }
    }

    return minPathSums[rowCount - 1][colCount - 1];
  }

  // Brute Force
  // cost(i,j)=grid[i][j]+min(cost(i+1,j),cost(i,j+1))
  // Time complexity : O(2^(m+n)) For every move, we have atmost 2 options.
  // Space complexity : O(m+n). Recursion of depth m+n.
  public int minPathSum(int[][] grid) {
    return this.calculateSum(grid, 0, 0);
  }

  private int calculateSum(int[][] grid, int row, int col) {
    if (row == grid.length || col == grid[0].length) {
      return Integer.MAX_VALUE;
    }

    if (row == grid.length - 1 && col == grid[0].length - 1) {
      return grid[row][col];
    }

    return (
      grid[row][col] +
      Math.min(
        this.calculateSum(grid, row + 1, col),
        this.calculateSum(grid, row, col + 1)
      )
    );
  }
}

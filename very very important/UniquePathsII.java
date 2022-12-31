// Array, Dynamic Programming, Matrix
// Amazon 9 Google 3 Facebook 2 Cruise Automation 8 Qualtrics 5 Cisco 3 Microsoft 2 Salesforce 2 Oracle 2 Athenahealth 2 Paypal 2 Bloomberg 3 Goldman Sachs 2 Apple 2 Zillow 2 ByteDance 2 Intuit 2
// https://leetcode.com/problems/unique-paths-ii/

// You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

// An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

// Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

// The testcases are generated so that the answer will be less than or equal to 2 * 109.

// Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
// Output: 2
// Explanation: There is one obstacle in the middle of the 3x3 grid above.
// There are two ways to reach the bottom-right corner:
// 1. Right -> Right -> Down -> Down
// 2. Down -> Down -> Right -> Right

class UniquePathsII {

  private class GridType {

    static int SPACE = 0; // static needed for reference
    static int WALL = 1; // static needed for reference
  }

  // dp
  // function(row, col) = function(row - 1, col) + function(row, col - 1) if current grid is not a wall
  public int uniquePathsWithObstacles(int[][] grid) {
    if (grid[0][0] == 1) {
      return 0;
    }

    int rowCount = grid.length;
    int colCount = grid[0].length;
    int[][] pathSums = new int[rowCount][colCount];
    pathSums[0][0] = 1;
    // once there is a wall, the following first col and row values will be 0
    for (int row = 1; row < rowCount; row++) {
      int prevPathSum = pathSums[row - 1][0];
      int gridVal = grid[row][0];
      if (gridVal == GridType.SPACE && prevPathSum != 0) {
        pathSums[row][0] = 1;
      } else {
        pathSums[row][0] = 0;
      }
    }
    for (int col = 1; col < colCount; col++) {
      int prevPathSum = pathSums[0][col - 1];
      int gridVal = grid[0][col];
      if (gridVal == GridType.SPACE && prevPathSum != 0) {
        pathSums[0][col] = 1;
      } else {
        pathSums[0][col] = 0;
      }
    }

    for (int row = 1; row < rowCount; row++) {
      for (int col = 1; col < colCount; col++) {
        int gridVal = grid[row][col];
        if (gridVal == GridType.SPACE) {
          pathSums[row][col] = pathSums[row - 1][col] + pathSums[row][col - 1];
        }
        if (gridVal == GridType.WALL) {
          pathSums[row][col] = 0;
        }
      }
    }

    return pathSums[rowCount - 1][colCount - 1];
  }

  // brute force
  public int uniquePathsWithObstacles(int[][] grid) {
    return this.getPathCount(grid, 0, 0);
  }

  private int getPathCount(int[][] grid, int row, int col) {
    if (row == grid.length || col == grid[0].length) {
      return 0;
    }

    if (grid[row][col] == GridType.WALL) {
      return 0;
    }

    if (row == grid.length - 1 && col == grid[0].length - 1) {
      return 1;
    }

    int countFromRight = this.getPathCount(grid, row, col + 1);
    int countFromDown = this.getPathCount(grid, row + 1, col);

    return countFromRight + countFromDown;
  }
}

// Math, Dynamic Programming, Combinatorics
// Amazon 16 Google 10 Adobe 6 Apple 5 Bloomberg 4 Yahoo 3 Facebook 2 TikTok 2 Cruise Automation 2 Trilogy 2 Microsoft 11 Goldman Sachs 2 Expedia 2 Infosys 2 ByteDance 4 Salesforce 3 Zillow 3 Oracle 3 Walmart Global Tech 2 VMware 2 Uber 2 Wish 2 Morgan Stanley 2 Zoho 2 Intuit 2
// https://leetcode.com/problems/unique-paths/description/

// There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]).
// The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
// Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
// The test cases are generated so that the answer will be less than or equal to 2 * 109.

// Input: m = 3, n = 2
// Output: 3
// Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
// 1. Right -> Down -> Down
// 2. Down -> Down -> Right
// 3. Down -> Right -> Down
class UniquePaths {

  // dp
  // state: row,col is the unique path count from 0,0 to row,col
  // function(row, col) = function(row - 1, col) + function(row, col - 1)
  // The robot can only move either down or right. Hence any cell in the first row can only be reached from the cell left to it.
  // And, any cell in the first column can only be reached from the cell above it.
  public int uniquePaths(int m, int n) {
    int[][] uniquePathCount = new int[m][n];
    uniquePathCount[0][0] = 1;
    for (int row = 1; row < m; row++) {
      uniquePathCount[row][0] = 1;
    }
    for (int col = 1; col < n; col++) {
      uniquePathCount[0][col] = 1;
    }

    for (int row = 1; row < m; row++) {
      for (int col = 1; col < n; col++) {
        uniquePathCount[row][col] =
          uniquePathCount[row - 1][col] + uniquePathCount[row][col - 1];
      }
    }

    return uniquePathCount[m - 1][n - 1];
  }

  // brute force
  // 2^(m+n) complexity
  // the first row and the first col has only one path(cannot move from top or left), so this can be used as the exit condition
  public int uniquePaths(int m, int n) {
    if (m == 1 || n == 1) {
      return 1;
    }

    return this.uniquePaths(m - 1, n) + this.uniquePaths(m, n - 1);
  }
}

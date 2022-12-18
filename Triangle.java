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

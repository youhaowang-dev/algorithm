// Backtracking
// Adobe 2 ByteDance 2 Zenefits
// https://leetcode.com/problems/n-queens-ii/
// The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

// Given an integer n, return the number of distinct solutions to the n-queens puzzle.

// Example 1:
// Input: n = 4
// Output: 2
// Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
// Example 2:
// Input: n = 1
// Output: 1
class NQueensII {

  public int totalNQueens(int n) {
    Set<Integer> columns = new HashSet<Integer>();
    Set<Integer> diagonals1 = new HashSet<Integer>();
    Set<Integer> diagonals2 = new HashSet<Integer>();
    int startRowIndex = 0;
    return this.getSolutionCount(
        n,
        startRowIndex,
        columns,
        diagonals1,
        diagonals2
      );
  }

  public int getSolutionCount(
    int targetQueens,
    int row,
    Set<Integer> columns,
    Set<Integer> diagonals1,
    Set<Integer> diagonals2
  ) {
    if (row == targetQueens) {
      return 1;
    }
    int count = 0;
    for (int i = 0; i < targetQueens; i++) {
      if (columns.contains(i)) {
        continue;
      }
      int diagonal1 = row - i;
      if (diagonals1.contains(diagonal1)) {
        continue;
      }
      int diagonal2 = row + i;
      if (diagonals2.contains(diagonal2)) {
        continue;
      }

      columns.add(i);
      diagonals1.add(diagonal1);
      diagonals2.add(diagonal2);

      count +=
        this.getSolutionCount(
            targetQueens,
            row + 1,
            columns,
            diagonals1,
            diagonals2
          );

      columns.remove(i);
      diagonals1.remove(diagonal1);
      diagonals2.remove(diagonal2);
    }

    return count;
  }
}

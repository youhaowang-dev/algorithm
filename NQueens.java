// Array, putQueensing
// Adobe 6 Amazon 4 Google 2 Microsoft 2 Bloomberg 2 Facebook 4 Apple 3 TikTok 3 Uber 2 ByteDance 2 Goldman Sachs 2
// https://leetcode.com/problems/n-queens/

// The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

// Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

// Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

// Example 1:
// Input: n = 4
// Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
// Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
// Example 2:
// Input: n = 1
// Output: [["Q"]]
class NQueens {

  // brute force: generate all board states
  // There are 62 * 61 * ... * 57 = 44,261,653,680 possible ways to place the remaining 6 queens

  // dfs
  // time O(n!)
  // space O(n^2)
  // index formular
  // [0,Q,0] Q at [0,1], so same row and col is under attack
  // [0,0,0] for diagnoals, [1,0] and [1,2] are under attack, so col index 0 and 2 cannot be used
  // [0,0,0] as a result the formulars are row(1)+1 and row(1)-1
  public List<List<String>> solveNQueens(int n) {
    List<List<String>> solutions = new ArrayList<>();
    int[] queens = new int[n];
    Arrays.fill(queens, -1);
    // sets to record the under attack col index
    Set<Integer> columns = new HashSet<>();
    Set<Integer> diagonals1 = new HashSet<>();
    Set<Integer> diagonals2 = new HashSet<>();
    int startRowIndex = 0;
    this.putQueens(
        solutions,
        queens,
        n,
        startRowIndex,
        columns,
        diagonals1,
        diagonals2
      );

    return solutions;
  }

  public void putQueens(
    List<List<String>> solutions,
    int[] queens,
    int queenCount,
    int row,
    Set<Integer> columns,
    Set<Integer> diagonals1,
    Set<Integer> diagonals2
  ) {
    // of course no row can have more than one queen
    // if we are able to put n queens in n rows, that is a solution
    if (row == queenCount) {
      List<String> board = this.getBoard(queens, queenCount);
      solutions.add(board);
      return;
    }
    // try to put n queens
    for (int i = 0; i < queenCount; i++) {
      if (columns.contains(i)) {
        continue;
      }
      // diagonal formular 1 row - i
      int diagonal1 = row - i;
      if (diagonals1.contains(diagonal1)) {
        continue;
      }
      // diagonal formular 2 row + i
      int diagonal2 = row + i;
      if (diagonals2.contains(diagonal2)) {
        continue;
      }
      // put queen
      queens[row] = i;
      columns.add(i);
      diagonals1.add(diagonal1);
      diagonals2.add(diagonal2);

      this.putQueens(
          solutions,
          queens,
          queenCount,
          row + 1,
          columns,
          diagonals1,
          diagonals2
        );
      // undo put queen
      queens[row] = -1;
      columns.remove(i);
      diagonals1.remove(diagonal1);
      diagonals2.remove(diagonal2);
    }
  }

  public List<String> getBoard(int[] queens, int n) {
    List<String> board = new ArrayList<String>();
    for (int i = 0; i < n; i++) {
      char[] row = new char[n];
      Arrays.fill(row, '.');
      row[queens[i]] = 'Q';
      board.add(new String(row));
    }

    return board;
  }
}

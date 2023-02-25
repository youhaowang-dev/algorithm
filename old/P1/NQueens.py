# Array, putQueensing
# Adobe 6 Amazon 4 Google 2 Microsoft 2 Bloomberg 2 Facebook 4 Apple 3 TikTok 3 Uber 2 ByteDance 2 Goldman Sachs 2
# https://leetcode.com/problems/n-queens/

# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

# Example 1:
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
# Example 2:
# Input: n = 1
# Output: [["Q"]]

# brute force: generate all board states
# O((n*n)!)
# There are 62 * 61 * ... * 57 = 44,261,653,680 possible ways to place the remaining 6 queens

# dfs try to put a queen in every row because same row cannot have 2 queens
# time O(n^2*n!) factorial, putting a queen reduces the choices for next queen, so n!, n^2 is for building the output
# space O(n^2) for board
class NQueens:
    QUEEN = "Q"
    SPACE = "."

    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 0:
            return []
        if n == 1:
            return [[self.QUEEN]]

        row = [self.SPACE for _ in range(n)]
        board = [list(row) for _ in range(n)]
        start_row = 0
        results = list()
        col_used = set()
        diagonal1_col_used = set()  # row + col
        diagonal2_col_used = set()  # row - col
        self.build_results(n, start_row, results, board,
                           col_used, diagonal1_col_used, diagonal2_col_used)

        return results

    def build_results(self, n, row, results, board, col_used, diagonal1_col_used, diagonal2_col_used):
        if row == n:
            # outbound means we are able to put all queens in all rows
            result = ["".join(row) for row in board]
            results.append(result)

        for col in range(n):
            if col in col_used or row + col in diagonal1_col_used or row - col in diagonal2_col_used:
                continue
            board[row][col] = self.QUEEN
            col_used.add(col)
            diagonal1_col_used.add(row + col)
            diagonal2_col_used.add(row - col)
            self.build_results(n, row + 1, results, board,
                               col_used, diagonal1_col_used, diagonal2_col_used)
            board[row][col] = self.SPACE
            col_used.remove(col)
            diagonal1_col_used.remove(row + col)
            diagonal2_col_used.remove(row - col)

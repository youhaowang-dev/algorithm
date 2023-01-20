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

# dfs
# time O(n!) factorial
# space O(n^2)
# index formular
# [0,Q,0] Q at [0,1], so same row and col is under attack
# [0,0,0] for diagnoals, [1,0] and [1,2] are under attack, so col index 0 and 2 cannot be used
# [0,0,0] as a result the formulars are row(1)+1 and row(1)-1
# no row can have more than one queen
# if we are able to put n queens in n rows, that is a solution
from ast import List


class NQueens:
    DEFAULT_INDEX = -1
    DEFAULT_CELL = "."
    QUEEN_CELL = "Q"

    def solveNQueens(self, n: int) -> List[List[str]]:
        results = list()
        if not n:
            return results

        # indices for col, row indices are 0,1,2,...n-1
        queens_col_indices = [self.DEFAULT_INDEX for _ in range(n)]
        col_underattack = set()
        diagonal1_col_underattack = set()
        diagonal2_col_underattack = set()
        start_row_index = 0
        self.put_queens(
            results,
            queens_col_indices,
            n,
            col_underattack,
            diagonal1_col_underattack,
            diagonal2_col_underattack,
            start_row_index,
        )

        return results

    def put_queens(
        self,
        results,
        queens_col_indices,
        queens_count,
        col_underattack,
        diagonal1_col_underattack,
        diagonal2_col_underattack,
        row_index,
    ):
        # of course no row can have more than one queen
        # if we are able to put n queens in n rows, that is a solution
        if row_index == queens_count:
            result = self.get_result(queens_col_indices)
            results.append(result)
        # try put queen on board
        for i in range(queens_count):
            if i in col_underattack:
                continue
            diagonal1_col = row_index - i
            if diagonal1_col in diagonal1_col_underattack:
                continue
            diagonal2_col = row_index + i
            if diagonal2_col in diagonal2_col_underattack:
                continue
            # put queen
            queens_col_indices[row_index] = i
            col_underattack.add(i)
            diagonal1_col_underattack.add(diagonal1_col)
            diagonal2_col_underattack.add(diagonal2_col)

            self.put_queens(
                results,
                queens_col_indices,
                queens_count,
                col_underattack,
                diagonal1_col_underattack,
                diagonal2_col_underattack,
                row_index + 1,
            )
            # unput queen
            queens_col_indices[row_index] = self.DEFAULT_INDEX
            col_underattack.remove(i)
            diagonal1_col_underattack.remove(diagonal1_col)
            diagonal2_col_underattack.remove(diagonal2_col)

    # put one queen on each row based on the col indices
    def get_result(self, queens_col_indices):
        result = list()
        default_row = row = [self.DEFAULT_CELL for _ in range(len(queens_col_indices))]
        for queen_col_index in queens_col_indices:
            row = list(default_row)
            row[queen_col_index] = self.QUEEN_CELL
            result.append("".join(row))

        return result

# Array, Hash Table, Matrix
# Amazon 9 Bloomberg 3 Microsoft 2 Apple 2 Adobe 2 Facebook 3 Oracle 2 Samsung 4 Goldman Sachs 3 Qualtrics 3
# Expedia 2 Google 2 VMware 2 Myntra 2 Juspay 2 Infosys 2
# https://leetcode.com/problems/set-matrix-zeroes/
# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place.

# Example 1:
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
# Example 2:
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]


# The idea is that we can use the first cell of every row and column as a flag.
# This flag would determine whether a row or column has been set to zero.
# This means for every cell instead of going to M+N cells and setting it to zero we just set the flag in two cells.
# if matrix[i][j] == 0, then matrix[0][j] = 0 and matrix[i][0] = 0

from ast import List, Tuple


class SetMatrixZeroes:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        first_row_has_zero, first_col_has_zero = self.set_marks(matrix)
        self.set_zeros(matrix, first_row_has_zero, first_col_has_zero)

    def set_marks(self, matrix):
        row_count = len(matrix)
        col_count = len(matrix[0])
        first_row_has_zero = False
        first_col_has_zero = False

        for row in range(row_count):
            for col in range(col_count):
                if matrix[row][col] == 0:
                    if row == 0:
                        first_row_has_zero = True
                    if col == 0:
                        first_col_has_zero = True
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        return (first_row_has_zero, first_col_has_zero)

    def set_zeros(self, matrix, first_row_has_zero, first_col_has_zero):
        row_count = len(matrix)
        col_count = len(matrix[0])
        # process first row and col later
        for row in range(1, row_count):
            for col in range(1, col_count):
                matrix[row][col] = (
                    0
                    if matrix[0][col] == 0 or matrix[row][0] == 0
                    else matrix[row][col]
                )

        if first_row_has_zero:
            for col in range(col_count):
                matrix[0][col] = 0

        if first_col_has_zero:
            for row in range(row_count):
                matrix[row][0] = 0


# brute force need extra space: If any cell of the matrix has a zero we can record its row and column number.
# All the cells of this recorded row and column can be marked zero in the next iteration.
class SetMatrixZeroes2:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # input validation
        if not matrix:
            return []

        m = len(matrix)
        n = len(matrix[0])
        zeroes_row = [False] * m
        zeroes_col = [False] * n
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    zeroes_row[row] = True
                    zeroes_col[col] = True

        for row in range(m):
            for col in range(n):
                if zeroes_row[row] or zeroes_col[col]:
                    matrix[row][col] = 0

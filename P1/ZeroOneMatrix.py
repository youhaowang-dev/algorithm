# Array, Dynamic Programming, Breadth-First Search, Matrix
# Amazon 6 Bloomberg 2 DoorDash 2 Google 6 Microsoft 2 Facebook 2 Adobe 2 Dunzo 2 Uber 3 Apple 3
# https://leetcode.com/problems/01-matrix/

# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

# The distance between two adjacent cells is 1.

# Example 1:
# Input: mat = [[0,0,0],
#               [0,1,0],
#               [0,0,0]]
# Output: [[0,0,0],
#          [0,1,0],
#          [0,0,0]]

# Example 2:
# Input: mat = [[0,0,0],
#               [0,1,0],
#               [1,1,1]]
# Output: [[0,0,0],
#          [0,1,0],
#          [1,2,1]]

from collections import deque
import math
from typing import List

# bfs
# https://leetcode.com/problems/01-matrix/solutions/1369741/c-java-python-bfs-dp-solutions-with-picture-clean-concise-o-1-space
# Same idea with Topology Sort, we process zero-cells first, then we use queue data structure to keep the order
# of processing cells, so that cells which have the smaller distance will be processed first.
class ZeroOneMatrix:
    DIRECTION_DELTAS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    TO_BE_PROCESSED = -1

    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return matrix

        row_count = len(matrix)
        col_count = len(matrix[0])

        queue = deque()
        for row in range(row_count):
            for col in range(col_count):
                if matrix[row][col] == 0:
                    queue.append((row, col))
                else:
                    matrix[row][col] = self.TO_BE_PROCESSED

        while queue:
            row, col = queue.popleft()
            for row_delta, col_delta in self.DIRECTION_DELTAS:
                new_row = row + row_delta
                new_col = col + col_delta
                if (
                    new_row < 0
                    or new_row >= row_count
                    or new_col < 0
                    or new_col >= col_count
                    or matrix[new_row][new_col] != self.TO_BE_PROCESSED
                ):
                    continue

                matrix[new_row][new_col] = matrix[row][col] + 1
                queue.append((new_row, new_col))

        return matrix


# dp
class ZeroOneMatrix2:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return matrix

        row_count = len(matrix)
        col_count = len(matrix[0])

        for row in range(row_count):
            for col in range(col_count):
                if matrix[row][col] > 0:
                    top = matrix[row - 1][col] if row > 0 else math.inf
                    left = matrix[row][col - 1] if col > 0 else math.inf
                    matrix[row][col] = min(top, left) + 1

        for row in range(row_count - 1, -1, -1):
            for col in range(col_count - 1, -1, -1):
                if matrix[row][col] > 0:
                    bottom = matrix[row + 1][col] if row < row_count - 1 else math.inf
                    right = matrix[row][col + 1] if col < col_count - 1 else math.inf
                    matrix[row][col] = min(matrix[row][col], bottom + 1, right + 1)

        return matrix

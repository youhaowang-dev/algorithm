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

# bfs, process from 0 distance to more distance cells like topologic sort
# current distance = neighbor distance + 1
# 0, 0, 0            0, 0, 0          0, 0, 0           0, 0, 0        0, 0, 0
# 0, -1, 0     =>    0, 1, 0    =>    0, 1, 0     =>    0, 1, 0   =>   0, 1, 0
# -1, -1, -1        -1, -1, -1        1, -1, -1         1, -1, 1       1, 2, 1
class ZeroOneMatrix:
    WAS_ONE = -1  # distance can be 0,1,2,3... so -1 won't be used

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
                elif matrix[row][col] == 1:
                    matrix[row][col] = self.WAS_ONE

        while queue:  # bfs, matrix[was one] = matrix[prev distance] + 1
            row, col = queue.popleft()
            for row_delta, col_delta in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_row = row + row_delta
                new_col = col + col_delta
                if (
                    new_row < 0
                    or new_row >= row_count
                    or new_col < 0
                    or new_col >= col_count
                ):
                    continue

                if matrix[new_row][new_col] != self.WAS_ONE:
                    continue

                matrix[new_row][new_col] = 1 + matrix[row][col]
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
                    bottom = matrix[row +
                                    1][col] if row < row_count - 1 else math.inf
                    right = matrix[row][col +
                                        1] if col < col_count - 1 else math.inf
                    matrix[row][col] = min(
                        matrix[row][col], bottom + 1, right + 1)

        return matrix

# Array, Math, Matrix
# Amazon 13 Cisco 10 Adobe 8 Microsoft 4 Bloomberg 4 Apple 3 Uber 2 Square 2 Roblox 2 Facebook 11 Google 6 Epam Systems 3
# Rubrik 2 Oracle 2 Nvidia 2 Paypal 2 TikTok 2 Tiger Analytics 2 Yahoo 2 eBay 3 Houzz 2 ServiceNow 2 Akuna Capital 2
# Databricks 2 Citadel 2 Snapchat 2 Asana 2 VMware 2 DE Shaw 2 ByteDance 2
# https://leetcode.com/problems/rotate-image/

# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
# DO NOT allocate another 2D matrix and do the rotation.

# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
# Example 2:
# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

from typing import List
import copy


# clockwise rotation, swap rows then swap diagonal cells
# 1 2 3     7 8 9     7 4 1
# 4 5 6  => 4 5 6  => 8 5 2
# 7 8 9     1 2 3     9 6 3
class RotateImage:
    def rotate(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return

        matrix.reverse()
        self.swap_diag(matrix)

    def swap_diag(self, matrix):
        for row in range(len(matrix)):
            for col in range(row):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]


# counter clockwise rotate, swap cols then swap digonal cells
# 1 2 3     3 2 1     3 6 9
# 4 5 6  => 6 5 4  => 2 5 8
# 7 8 9     9 8 7     1 4 7
class RotateImage2:
    def rotate(self, matrix: List[List[int]]) -> None:
        self.reverse_rows(matrix)
        self.swap_diagonals(matrix)

    def reverse_rows(self, matrix: List[List[int]]):
        for row in matrix:
            row.reverse()

    def swap_diagonals(self, matrix: List[List[int]]):
        for row in range(len(matrix)):
            for col in range(row):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

copy1 = copy.deepcopy(matrix)
assert RotateImage().rotate(copy1) == None
assert copy1 == [[7, 4, 1],
                 [8, 5, 2],
                 [9, 6, 3]]

copy2 = copy.deepcopy(matrix)
assert RotateImage2().rotate(copy2) == None
assert copy2 == [[3, 6, 9],
                 [2, 5, 8],
                 [1, 4, 7]]
print("DONE")

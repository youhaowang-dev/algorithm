# Array, Binary Search, Matrix
# Amazon 17 Apple 8 Bloomberg 5 Microsoft 3 Google 3 Adobe 3 Visa 2 Walmart Global Tech 2
# https://leetcode.com/problems/search-a-2d-matrix/
# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:
#             Integers in each row are sorted from left to right.
#             The first integer of each row is greater than the last integer of the previous row.
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3, Output: true
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13, Output: false
from typing import List


class SearchA2DMatrix:

    # brute force linear search each row and its cols
    # time O(row_count * col_count)

    # binary search time O(log(row_count * col_count))
    # given the matrix properties
    # binary search can be used on the sorted array
    # need to take care of 1D => 2D conversion
    def searchMatrix(self, matrix: List[List[int]], target: int) -> int:
        if not matrix or not matrix[0]:
            return False

        total_len = len(matrix) * len(matrix[0])
        left = 0
        right = total_len - 1
        while left + 1 < right:
            mid = (left + right) // 2
            midVal = self.get_val(matrix, mid)
            if midVal == target:
                return True

            if midVal < target:
                left = mid

            if midVal > target:
                right = mid

        # left == right or left+1 == right
        if self.get_val(matrix, left) == target:
            return True

        if self.get_val(matrix, right) == target:
            return True

        return False

    # get matrix value by using 1D index
    # given [[1,2,3],[4,5,6],[7,8,9]]
    # index = 3 => rowIndex = 1, colIndex = 0 => rowIndex = index / col_count = 3/3 = 1, colIndex = index % col_count = 3%3=0
    # index = 5 => expect value = 6, expect rowIndex = 1 = 5 / 3, colIndex = 2 = 5 % 3
    def get_val(self, matrix: List[List[int]], index: int) -> int:
        if not matrix or not matrix[0]:
            return False

        row_count = len(matrix)
        col_count = len(matrix[0])
        if index < 0 or index >= row_count * col_count:
            return float("inf")

        rowIndex = index // col_count
        colIndex = index % col_count

        return matrix[rowIndex][colIndex]

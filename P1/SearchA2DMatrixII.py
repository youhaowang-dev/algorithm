# Array, Binary Search, Divide and Conquer, Matrix
# Amazon 6 Microsoft 5 Bloomberg 3 Adobe 3 Zillow 2 Apple 3 Oracle 3 Google 2 PayTM 2 Facebook 7 ByteDance 7 Goldman Sachs 3 Paypal 2 Salesforce 2 Uber 2 Nvidia 2
# https://leetcode.com/problems/search-a-2d-matrix-ii/
# Write an efficient algorithm that searches for a val target in an m x n integer matrix matrix. This matrix has the following properties:
#              Integers in each row are sorted in ascending from left to right.
#              Integers in each column are sorted in ascending from top to bottom.
# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5, Output: true
# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20, Output: false
from ast import List


class SearchA2DMatrixII:

    # Because the rows and columns of the matrix are sorted (from left-to-right and top-to-bottom, respectively),
    # we can prune O(m) or O(n) elements when looking at any particular val.

    # pick top-right or the bottom-left corner as the "middle" vals
    # move rowIndex and colIndex based on comparision
    # O(rowCount + columnCount)
    # https://leetcode.com/problems/search-a-2d-matrix-ii/solutions/127690/search-a-2d-matrix-ii/
    # This would work equally well with a pointer initialized to the top-right.
    # Neither of the other two corners would work, as pruning a row/column might prevent us from achieving the correct answer.
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        # start position at bottom left corner, can only go up or go right
        rowIndex = len(matrix) - 1  # move up to become smaller
        colIndex = 0  # move right to become larger
        # >= <= because we still need to search in the first row or the last column
        while rowIndex >= 0 and colIndex <= len(matrix[0]) - 1:
            val = matrix[rowIndex][colIndex]
            if val == target:
                return True
            if val > target:
                # skip the row as all vals of the row right side are greater than target
                rowIndex -= 1
            if val < target:
                # check within the current row
                colIndex += 1

        return False

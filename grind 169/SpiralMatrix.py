# Array, Matrix, Simulation
# Amazon 12 Microsoft 4 Apple 4 Google 4 Adobe 4 Cisco 3 Bloomberg 2 Uber 2 Yahoo 2 Oracle 2 TikTok 2 Virtu Financial 2
# Facebook 7 Intuit 3 Zillow 2 Walmart Global Tech 2 Snapdeal 2 Epam Systems 2 Dunzo 2 VMware 5 LiveRamp 4 ByteDance 3
# Tesla 3 Nvidia 3 Epic Systems 2 eBay 2 Redfin 2 ServiceNow 2 SAP 2 Goldman Sachs 2 PayTM 2 Accolite 2 Flipkart 2 HBO 2
# https://leetcode.com/problems/spiral-matrix/

# Given an m x n matrix, return all elements of the matrix in spiral order.

# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]


# top bottom left right as boundaries
class SpiralMatrix:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return list()

        result = list()
        min_row = 0
        max_row = len(matrix) - 1
        min_col = 0
        max_col = len(matrix[0]) - 1
        while min_row <= max_row and min_col <= max_col:
            for i in range(min_col, max_col + 1):
                result.append(matrix[min_row][i])
            min_row += 1

            for i in range(min_row, max_row + 1):
                result.append(matrix[i][max_col])
            max_col -= 1

            if min_row <= max_row:
                for i in range(max_col, min_col - 1, -1):
                    result.append(matrix[max_row][i])
                max_row -= 1

            if min_col <= max_col:
                for i in range(max_row, min_row - 1, -1):
                    result.append(matrix[i][min_col])
                min_col += 1

        return result

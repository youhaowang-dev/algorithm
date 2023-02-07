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
        results = list()
        if not matrix:
            return results

        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        while top <= bottom and left <= right:
            # process top row
            for i in range(left, right + 1):
                results.append(matrix[top][i])
            top += 1
            # process right col
            for i in range(top, bottom + 1):
                results.append(matrix[i][right])
            right -= 1
            # process bottom row
            if top <= bottom:  # avoid duplicate
                for i in range(right, left - 1, -1):
                    results.append(matrix[bottom][i])
                bottom -= 1
            # process left col
            if left <= right:  # avoid duplicate
                for i in range(bottom, top - 1, -1):
                    results.append(matrix[i][left])
                left += 1

        return results


# same logic, trim the output, only take first n*m elements
class SpiralMatrix2:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        results = list()
        if not matrix:
            return results
        row_count = len(matrix)
        col_count = len(matrix[0])
        top = 0
        bottom = row_count - 1
        left = 0
        right = col_count - 1
        while top <= bottom and left <= right:
            # process top row
            for i in range(left, right + 1):
                results.append(matrix[top][i])
            top += 1
            # process right col
            for i in range(top, bottom + 1):
                results.append(matrix[i][right])
            right -= 1
            # process bottom row
            for i in range(right, left - 1, -1):
                results.append(matrix[bottom][i])
            bottom -= 1
            # process left col
            for i in range(bottom, top - 1, -1):
                results.append(matrix[i][left])
            left += 1

        # trim, only take first m*n element
        return results[: row_count * col_count]

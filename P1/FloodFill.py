# Array, Depth-First Search, Breadth-First Search, Matrix
# Amazon 9 Microsoft 3 Karat 3 Apple 2 Facebook 2 Bloomberg 3 Google 3 Qualtrics 2 Adobe 2 Oracle 4 Salesforce 3 Palantir Technologies 2 Nvidia 2 Netflix 2 Uber
# https://leetcode.com/problems/flood-fill/

# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

# You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting
# pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels
# (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

# Return the modified image after performing the flood fill.

# Example 1:
# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels
# connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

# Example 2:
# Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
# Output: [[0,0,0],[0,0,0]]
# Explanation: The starting pixel is already colored 0, so no changes are made to the image.

from typing import List


class FloodFill:
    def floodFill(
        self, image: List[List[int]], row: int, col: int, new_color: int
    ) -> List[List[int]]:
        if not image or not image[0]:
            return image

        if image[row][col] == new_color:
            return image

        self.dfs_fill(image, row, col, image[row][col], new_color)

        return image

    def dfs_fill(
        self, image: List[List[int]], row: int, col: int, color: int, new_color: int
    ) -> None:
        if (
            row < 0
            or row >= len(image)
            or col < 0
            or col >= len(image[0])
            or image[row][col] != color
        ):
            return

        image[row][col] = new_color
        self.dfs_fill(image, row + 1, col, color, new_color)
        self.dfs_fill(image, row - 1, col, color, new_color)
        self.dfs_fill(image, row, col + 1, color, new_color)
        self.dfs_fill(image, row, col - 1, color, new_color)

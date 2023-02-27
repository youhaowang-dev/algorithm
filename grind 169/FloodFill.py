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

# dfs, time: O(m*n) for each color can only be replaced once
# space: O(m*n) for a spiral image
class FloodFill:
    def floodFill(self, image: List[List[int]], row_start: int, col_start: int, new_color: int) -> List[List[int]]:
        if not image:
            return image

        old_color = image[row_start][col_start]
        if old_color == new_color:
            return image

        self.fill(image, row_start, col_start, old_color, new_color)

        return image

    def fill(self, image, row, col, old_color, new_color):
        if not (
            0 <= row < len(image) and
            0 <= col < len(image[0])
        ):
            return
        if image[row][col] != old_color:
            return

        image[row][col] = new_color

        for row_delta, col_delta in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            self.fill(image, row + row_delta, col +
                      col_delta, old_color, new_color)

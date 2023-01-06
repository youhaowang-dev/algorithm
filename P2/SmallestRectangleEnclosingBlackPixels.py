# Array, Binary Search, Depth-First Search, Breadth-First Search, Matrix
# Google 2
# https://leetcode.com/problems/smallest-rectangle-enclosing-black-pixels/description/
# You are given an m x n binary matrix image where 0 represents a white pixel and 1 represents a black pixel.

# The black pixels are connected (i.e., there is only one black region). Pixels are connected horizontally and vertically.

# Given two integers x and y that represents the location of one of the black pixels, return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.

# You must write an algorithm with less than O(mn) runtime complexity


# Example 1:


# Input: image = [["0","0","1","0"],["0","1","1","0"],["0","1","0","0"]], x = 0, y = 2
# Output: 6
# Example 2:

# Input: image = [["1"]], x = 0, y = 0
# Output: 1

# brute force: linear scan
from ast import List


# linear scan O(m*n)
# Initialize left, right, top and bottom
# Loop through all (x, y) coordinates
#   if image[x][y] is black
#       left = min(left, x)
#       right = max(right, x + 1)
#       top = min(top, y)
#       bottom = max(bottom, y + 1)
#   Return (right - left) * (bottom - top)
class SmallestRectangleEnclosingBlackPixels:
    BLACK = "1"

    def minArea(self, image: List[List[int]], x: int, y: int) -> int:
        if not image or not image[0]:
            return 0

        top = x
        bottom = x
        left = y
        right = y
        for x in range(0, len(image)):
            for y in range(0, len(image[0])):
                if image[x][y] == self.BLACK:
                    top = min(top, x)
                    bottom = max(bottom, x + 1)
                    left = min(left, y)
                    right = max(right, y + 1)

        return (right - left) * (bottom - top)


# binary search O(mlogn + nlogm)
# If a row/column has any black pixel it's projection is black otherwise white.
# left, right: check if col has black
# top, bottom: check if row has black
class SmallestRectangleEnclosingBlackPixels2:
    BLACK = "1"

    # left right param can be left->right and top->bottom
    def get_first(self, image, left, right, check_func):
        while left + 1 < right:
            mid = (left + right) // 2
            if check_func(image, mid):
                right = mid
            else:
                left = mid
        # check last two items
        if check_func(image, left):
            return left
        return right

    def get_last(self, image, left, right, check_func):
        while left + 1 < right:
            mid = (left + right) // 2
            if check_func(image, mid):
                left = mid
            else:
                right = mid
        if check_func(image, right):
            return right
        return left

    def row_has_black(self, image, row):
        for i in range(len(image[0])):
            if image[row][i] == self.BLACK:
                return True
        return False

    def col_has_black(self, image, col):
        for i in range(len(image)):
            if image[i][col] == self.BLACK:
                return True
        return False

    def minArea(self, image: List[List[str]], x: int, y: int) -> int:

        left = self.get_first(image, 0, y, self.col_has_black)
        right = self.get_last(image, y, len(image[0]) - 1, self.col_has_black)

        top = self.get_first(image, 0, x, self.row_has_black)
        bottom = self.get_last(image, x, len(image) - 1, self.row_has_black)

        return (bottom - top + 1) * (right - left + 1)

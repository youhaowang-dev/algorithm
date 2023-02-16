# Array, Dynamic Programming, Stack, Matrix, Monotonic Stack
# Amazon 2 Google 4 Apple 3 Bloomberg 5 ByteDance 4 Dunzo 3 Adobe 2 Microsoft 2 Facebook 2 Yahoo 2 Uber 2 Walmart Global Tech 2 Arcesium 2
# https://leetcode.com/problems/maximal-rectangle/

# Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
# Example 1:
# Input: matrix = [["1", "0", "1", "0", "0"],
#                  ["1", "0", "1", "1", "1"],
#                  ["1", "1", "1", "1", "1"],
#                  ["1", "0", "0", "1", "0"]]
# Output: 6
# Explanation: The maximal rectangle is shown in the above picture.
# Example 2:
# Input: matrix = [["0"]]
# Output: 0
# Example 3:
# Input: matrix = [["1"]]
# Output: 1

# convert to Largest Rectangle in Histogram
class MaximalRectangle:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        max_area = 0
        heights = [0 for _ in range(len(matrix[0]))]
        for row in matrix:
            max_area = max(max_area, self.get_max_area(row, heights))

        return max_area

    def get_max_area(self, new_row, heights):
        # build the count based on new_row
        for i, count in enumerate(heights):
            if new_row[i] == "1":
                heights[i] += 1
            else:
                heights[i] = 0
        return self.get_max_rect_area(heights)

    def get_max_rect_area(self, heights: List[int]) -> int:
        max_area = 0
        if not heights:
            return max_area

        stack = deque()  # only contains height that can extend to the end, so the stack elements can only increase
        for i, height in enumerate(heights):
            start = i  # rectangle area start position
            while stack and stack[-1][1] > height:
                bigger_height_start_index, bigger_height = stack.pop()
                max_area = max(
                    max_area, (i - bigger_height_start_index) * bigger_height)
                start = bigger_height_start_index
            # push in stack when can make stack elements increasing
            stack.append((start, height))

        while stack:  # process the heights that can extend to end
            start, height = stack.pop()
            max_area = max(max_area, (len(heights) - start) * height)

        return max_area

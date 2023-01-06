// Array, Dynamic Programming, Stack, Matrix, Monotonic Stack
// Amazon 2 Google 4 Apple 3 Bloomberg 5 ByteDance 4 Dunzo 3 Adobe 2 Microsoft 2 Facebook 2 Yahoo 2 Uber 2 Walmart Global Tech 2 Arcesium 2
// https://leetcode.com/problems/maximal-rectangle/
//
// Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
// Example 1:
// Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
// Output: 6
// Explanation: The maximal rectangle is shown in the above picture.
// Example 2:
// Input: matrix = [["0"]]
// Output: 0
// Example 3:
// Input: matrix = [["1"]]
// Output: 1

class MaximalRectangle {

  public int maximalRectangle(char[][] matrix) {
    if (matrix.length == 0) {
      return 0;
    }
    int maxArea = 0;
    int row = matrix.length;
    int[] heights = new int[matrix[0].length];
    for (int i = 0; i < row; i++) {
      this.updateHeights(matrix, i, heights);
      maxArea = Math.max(maxArea, this.getMaxRectangleInHistogram(heights));
    }

    return maxArea;
  }

  private void updateHeights(char[][] matrix, int i, int[] heights) {
    for (int j = 0; j < matrix[0].length; j++) {
      // NOTE: matrix[i][j].equals('1') will throw for char cannot be dereferenced
      heights[j] = matrix[i][j] == '1' ? heights[j] + 1 : 0;
    }
  }

  private int getMaxRectangleInHistogram(int[] heights) {
    Stack<Integer> index = new Stack<>();
    int outBoundIndex = -1; // for init, and edge cases
    index.push(outBoundIndex);
    int maxArea = Integer.MIN_VALUE;

    // scan the heights and only keep the indexes of increasing heights
    for (int i = 0; i < heights.length; i++) {
      while (
        index.peek() != outBoundIndex && heights[i] <= heights[index.peek()]
      ) {
        // pop the small height and calculate area
        int height = heights[index.pop()]; // it is already the small height, so no need to min
        int width = i - index.peek() - 1;
        maxArea = Math.max(maxArea, height * width);
      }
      index.push(i);
    }
    // continue process all the increasing heights
    // for increasing heights, the max is always the height * widthToLastHighestIndex
    int lastHighestIndex = heights.length; // assume right bound is Integer.MAX_VALUE
    while (index.peek() != outBoundIndex) {
      int height = heights[index.pop()]; // smaller than Integer.MAX_VALUE
      int width = lastHighestIndex - index.peek() - 1;
      maxArea = Math.max(maxArea, height * width);
    }

    return maxArea;
  }
}

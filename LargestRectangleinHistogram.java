// Array, Stack, Monotonic Stack
// Amazon 9 Adobe 5 Apple 3 Facebook 3 DoorDash 3 Salesforce 3 Google 2 Microsoft 7 Bloomberg 4 Uber 4 Cisco 3 Flipkart 2 ByteDance 2 Roblox 2 eBay 3 MAQ Software 3 Twitter 2 Snapchat 2 Nvidia 2 HBO 2 TikTok 2
// https://leetcode.com/problems/largest-rectangle-in-histogram/description/

// Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

// Example 1:

// Input: heights = [2,1,5,6,2,3]
// Output: 10
// Explanation: The above is a histogram where width of each bar is 1.
// The largest rectangle is shown in the red area, which has an area = 10 units.

class LargestRectangleinHistogram {

  // brute force O(n^3)
  public int largestRectangleArea(int[] heights) {
    int maxArea = 0;
    for (int i = 0; i < heights.length; i++) {
      for (int j = i; j < heights.length; j++) {
        int minHeight = Integer.MAX_VALUE;
        for (int k = i; k <= j; k++) {
          minHeight = Math.min(minHeight, heights[k]);
        }
        maxArea = Math.max(maxArea, minHeight * (j - i + 1));
      }
    }

    return maxArea;
  }

  // the height of the rectangle formed between any two bars will always be limited by the height of the shortest bar lying between them
  // O(n)
  // stack to save the increasing heights only, calculate the max area when poping a height
  // increase heights means increasing area; otherwise no need to calculate until increasing ends or the array ends
  public int largestRectangleArea(int[] heights) {
    // saves the increasing indexes of heights; heights[i]>heights[i−1]
    Stack<Integer> index = new Stack<>();
    int outBoundIndex = -1; // as a start indicator
    index.push(outBoundIndex);
    int length = heights.length;
    int maxArea = 0;

    for (int i = 0; i < length; i++) {
      while (
        index.peek() != outBoundIndex && heights[i] <= heights[index.peek()]
      ) {
        // next height is smaller, calculate area now
        int height = heights[index.pop()];
        int width = i - index.peek() - 1;
        maxArea = Math.max(maxArea, height * width);
      }
      // heights[i]>heights[i−1]
      index.push(i);
    }

    // IMPORTANT: array can be incremental, so we need to calculate the areas until stack empty
    while (index.peek() != outBoundIndex) {
      int height = heights[index.pop()];
      int width = length - index.peek() - 1;
      maxArea = Math.max(maxArea, height * width);
    }

    return maxArea;
  }
}

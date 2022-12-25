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

# Array, Stack, Monotonic Stack
# Amazon 9 Adobe 5 Apple 3 Facebook 3 DoorDash 3 Salesforce 3 Google 2 Microsoft 7 Bloomberg 4 Uber 4 Cisco 3
# Flipkart 2 ByteDance 2 Roblox 2 eBay 3 MAQ Software 3 Twitter 2 Snapchat 2 Nvidia 2 HBO 2 TikTok 2
# https://leetcode.com/problems/largest-rectangle-in-histogram/description/

# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1,
# return the area of the largest rectangle in the histogram.

# Example 1:
# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.

# stack can only increasing, calculate areas and save the index, finally empty the stack
class LargestRectangleinHistogram:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        if not heights:
            return max_area

        stack = deque()  # only contains height that can extend to the end, so the stack elements can only increase
        for i, height in enumerate(heights):
            start = i  # rectangle area start position
            while stack and stack[-1][1] > height:
                bigger_height_index, bigger_height = stack.pop()
                max_area = max(
                    max_area, (i - bigger_height_index) * bigger_height)
                start = bigger_height_index
            # push in stack when can make stack elements increasing
            stack.append((start, height))

        while stack:  # process the heights that can extend to end
            start, height = stack.pop()
            max_area = max(max_area, (len(heights) - start) * height)

        return max_area


# brute force: try every i,j pair
# time n^3 space 1
class LargestRectangleinHistogram2:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0

        length = len(heights)
        max_area = 0
        for start in range(length):
            for end in range(start, length):
                max_area = max(max_area, self.get_area(heights, start, end))

        return max_area

    def get_area(self, heights, start, end):
        width = end - start + 1  # need to include self, width=1
        min_height = min(heights[start:end + 1])
        return min_height * width

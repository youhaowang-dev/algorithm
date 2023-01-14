# Array, Design, Binary Indexed Tree, Segment Tree
# Amazon 2 Google 4 Adobe 2 Facebook 2
# https://leetcode.com/problems/range-sum-query-mutable/description/

# Given an integer array nums, handle multiple queries of the following types:

# Update the value of an element in nums.
# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:

# NumArray(int[] nums) Initializes the object with the integer array nums.
# void update(int index, int val) Updates the value of nums[index] to be val.
# int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

# Example 1:
# Input
# ["NumArray", "sumRange", "update", "sumRange"]
# [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
# Output
# [null, 9, null, 8]
# Explanation
# NumArray numArray = new NumArray([1, 3, 5]);
# numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
# numArray.update(1, 2);   // nums = [1, 2, 5]
# numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8


from typing import List

# segment tree node
class Node(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.left = None
        self.right = None


class NumArray(object):
    def __init__(self, nums):
        def createTree(nums, l, r):

            # base case
            if l > r:
                return None

            # leaf node
            if l == r:
                n = Node(l, r)
                n.total = nums[l]
                return n

            mid = (l + r) // 2

            root = Node(l, r)

            root.left = createTree(nums, l, mid)
            root.right = createTree(nums, mid + 1, r)

            root.total = root.left.total + root.right.total

            return root

        self.root = createTree(nums, 0, len(nums) - 1)

    def update(self, i, val):
        # recursively update total
        def updateVal(root, i, val):

            # leaf
            if root.start == root.end:
                root.total = val
                return

            mid = (root.start + root.end) // 2

            # need to update left subtree
            if i <= mid:
                updateVal(root.left, i, val)

            # need to update right subtree
            else:
                updateVal(root.right, i, val)

            # recursively update total
            root.total = root.left.total + root.right.total

        updateVal(self.root, i, val)

    def sumRange(self, i, j):
        # Helper function to calculate range sum
        def rangeSum(root, i, j):

            # If the range exactly matches the root, we already have the sum
            if root.start == i and root.end == j:
                return root.total

            mid = (root.start + root.end) // 2

            # end <= mid, search left subtree
            if j <= mid:
                return rangeSum(root.left, i, j)

            # start > mid, search right subtree
            elif i >= mid + 1:
                return rangeSum(root.right, i, j)

            # sum both sides
            else:
                return rangeSum(root.left, i, mid) + rangeSum(root.right, mid + 1, j)

        return rangeSum(self.root, i, j)

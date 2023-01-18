# Tree, Depth-First Search, Breadth-First Search, Binary Tree
# Amazon 6 Google 3 Bloomberg 2 Microsoft 8 Facebook 7 Walmart Global Tech 2
# https://leetcode.com/problems/path-sum/
# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path
# such that adding up all the values along the path equals targetSum.

# A leaf is a node with no children.
from collections import deque
from typing import Deque, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# bfs
class PathSum:
    def hasPathSum(self, root: Optional[TreeNode], target: int) -> bool:
        if not root:
            return False

        queue: Deque[TreeNode, int] = deque()
        queue.append((root, 0 + root.val))
        while queue:
            node, path_sum = queue.popleft()
            if self.is_leaf(node) and path_sum == target:
                return True
            if node.left:
                queue.append((node.left, node.left.val + path_sum))
            if node.right:
                queue.append((node.right, node.right.val + path_sum))

        return False

    def is_leaf(self, node: TreeNode):
        return not node.left and not node.right


# dfs
class PathSum2:
    def hasPathSum(self, root: Optional[TreeNode], target: int) -> bool:
        if not root:
            return False

        target_remain = target - root.val
        if not root.left and not root.right:
            return target_remain == 0

        left_has_sum = self.hasPathSum(root.left, target_remain)
        right_has_sum = self.hasPathSum(root.right, target_remain)

        return left_has_sum or right_has_sum

# Tree, Depth-First Search, Breadth-First Search, Binary Tree
# Amazon 3 Facebook 3 Bloomberg 2 Goldman Sachs 3 Adobe 2
# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 2
# Example 2:
# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5

from collections import deque
from typing import Deque, Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# dfs
class MinimumDepthofBinaryTree:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        min_depth = 2**31 - 1
        # one is null
        if root.left:
            min_depth = min(min_depth, self.minDepth(root.left))
        if root.right:
            min_depth = min(min_depth, self.minDepth(root.right))
        # none is null
        return min_depth + 1


# bfs
class MinimumDepthofBinaryTree2:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        bfs_level_count = 0
        if not root:
            return bfs_level_count

        queue = deque()
        queue.append(root)
        while queue:
            bfs_level_count += 1
            level_node_count = len(queue)
            for _ in range(0, level_node_count):
                node = queue.popleft()
                if not node.left and not node.right:
                    return bfs_level_count  # found
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return bfs_level_count


# iterative dfs
class MinimumDepthofBinaryTree3:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack: Deque[Tuple[TreeNode, int]] = deque()
        stack.append((root, 1))
        min_depth = 2**31 - 1
        while stack:
            node, depth = stack.pop()
            if not node.left and not node.right:
                min_depth = min(min_depth, depth)
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))

        return min_depth

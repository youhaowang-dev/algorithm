# Tree, Depth-First Search, Breadth-First Search, Binary Tree
# Amazon 2 Adobe 3 Yahoo 2 Bloomberg 2 Apple 2 Microsoft
# https://leetcode.com/problems/find-bottom-left-tree-value/

# Given the root of a binary tree, return the leftmost value in the last row of the tree.

# Example 1:
# Input: root = [2,1,3]
# Output: 1

# Example 2:
# Input: root = [1,2,3,4,null,5,6,null,null,7]
# Output: 7

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindBottomLeftTreeValue:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return float("-inf")

        queue = deque()
        queue.append(root)
        result = root.val
        while queue:
            nodes = self.get_current_level_nodes(queue)
            result = nodes[0].val
            for node in nodes:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result

    def get_current_level_nodes(self, queue) -> List[int]:
        nodes = list()
        while queue:
            nodes.append(queue.popleft())

        return nodes

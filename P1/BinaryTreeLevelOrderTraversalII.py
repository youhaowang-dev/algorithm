# Tree, Breadth-First Search, Binary Tree
# Amazon 4 Apple 4 Microsoft 3
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

# Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTreeLevelOrderTraversalII:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = deque()
        if not root:
            return result

        queue = deque()
        queue.append(root)
        while queue:
            currentLevelNodes = self.getCurrentLevelNodes(queue)
            currentLevelResult = list()
            for node in currentLevelNodes:
                currentLevelResult.append(node.val)
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.appendleft(currentLevelResult)

        return result

    def getCurrentLevelNodes(self, queue) -> List[TreeNode]:
        nodes = list()
        while queue:
            nodes.append(queue.popleft())

        return nodes

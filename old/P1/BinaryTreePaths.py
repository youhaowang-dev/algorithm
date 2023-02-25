# String, Backtracking, Tree, Depth-First Search, Binary Tree
# Amazon 3 Capital One 2 Bloomberg 6 Google 2 Microsoft 2 Facebook 6 Apple 4
# https://leetcode.com/problems/binary-tree-paths/
# Given the root of a binary tree, return all root-to-leaf paths in any order.
# A leaf is a node with no children.
#
# Example 1:
# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]
# Example 2:
# Input: root = [1]
# Output: ["1"]

from ast import List
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTreePaths:
    DELIMITER = "->"

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        results = list()
        if not root:
            return results

        self.build_results(results, root)

        return results

    def build_results(self, results, root):
        queue = deque()
        queue.append((root, ""))
        while queue:
            node, path = queue.popleft()
            next_path = path + str(node.val)
            if not node.left and not node.right:
                results.append(next_path)
            if node.left:
                queue.append((node.left, next_path + self.DELIMITER))
            if node.right:
                queue.append((node.right, next_path + self.DELIMITER))

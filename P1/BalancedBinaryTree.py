# Tree, Depth-First Search, Binary Tree
# Amazon 4 Facebook 3 Google 3 Spotify 3 Uber 2 Bloomberg 2 Adobe 2 Microsoft 3
# https://leetcode.com/problems/balanced-binary-tree/
# Given a binary tree, determine if it is height-balanced.

from collections import deque
from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BalancedBinaryTree:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced, _ = self.isBalancedHelper(root)

        return is_balanced

    def isBalancedHelper(self, root: Optional[TreeNode]) -> Tuple[bool, int]:
        if root is None:
            return (True, 0)

        left_is_balanced, left_height = self.isBalancedHelper(root.left)
        right_is_balanced, right_height = self.isBalancedHelper(root.right)
        current_height = 1 + max(left_height, right_height)

        is_balanced = (
            left_is_balanced
            and right_is_balanced
            and abs(left_height - right_height) < 2
        )

        return (is_balanced, current_height)


class BalancedBinaryTree2:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right)
        root_balanced = abs(left_height - right_height) < 2
        left_balanced = self.isBalanced(root.left)
        right_balanced = self.isBalanced(root.right)

        return root_balanced and left_balanced and right_balanced

    # max depth of the tree
    def get_height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right)

        return 1 + max(left_height, right_height)


# iterative post order traversal
class BalancedBinaryTree3:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        stack, node, last, depths = deque(), root, None, dict()
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack[-1]
                if not node.right or last == node.right:
                    node = stack.pop()
                    left, right = depths.get(node.left, 0), depths.get(node.right, 0)
                    if abs(left - right) > 1:
                        return False
                    depths[node] = 1 + max(left, right)
                    last = node
                    node = None
                else:
                    node = node.right
        return True

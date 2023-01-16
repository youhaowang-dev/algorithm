# Stack, Tree, Depth-First Search, Binary Tree
# Google 3 Adobe 2 Apple 2 Amazon 4 Bloomberg 3 Microsoft 2
# https://leetcode.com/problems/binary-tree-preorder-traversal/

# Given the root of a binary tree, return the preorder traversal of its nodes' values.

from collections import deque
from typing import Deque, List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# iterative, add node.val to result, and push right util null, and go to left
# when null, pop and push
class BinaryTreePreorderTraversal:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = list()
        if not root:
            return result

        stack = deque()
        self.add_roots_and_push_rights(root, stack, result)
        while stack:
            node = stack.pop()
            self.add_roots_and_push_rights(node, stack, result)

        return result

    def add_roots_and_push_rights(
        self, root: TreeNode, stack: Deque, result: List[int]
    ) -> None:
        while root:
            result.append(root.val)  # 1 root
            stack.append(root.right)  # 3 right
            root = root.left  # 2 left


# recursion
class BinaryTreePreorderTraversal2:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = list()
        if not root:
            return result

        self.preorderTraversalHelper(root, result)

        return result

    def preorderTraversalHelper(self, root: TreeNode, result: List[int]) -> None:
        if not root:
            return

        result.append(root.val)
        self.preorderTraversalHelper(root.left, result)
        self.preorderTraversalHelper(root.right, result)


class BinaryTreePreorderTraversal3:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = list()
        if not root:
            return result

        left_result = self.preorderTraversal(root.left)
        right_result = self.preorderTraversal(root.right)
        result.append(root.val)
        result.extend(left_result)
        result.extend(right_result)

        return result

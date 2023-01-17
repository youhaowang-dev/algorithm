# Stack, Tree, Depth-First Search, Binary Tree
# Amazon 8 Adobe 4 Google 3 Facebook 2 Microsoft 2 Apple 3 Yahoo 2
# https://leetcode.com/problems/binary-tree-inorder-traversal/
# Given the root of a binary tree, return the inorder traversal of its nodes' values.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque
from typing import Deque, List, Optional


# while left is available, keep pushing lefts into stack
# when left is not available, pop a node and keep pushing the lefts of the node.right
class BinaryTreeInorderTraversal:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = list()
        if not root:
            return result

        stack = deque()
        self.push_roots(root, stack)
        while stack:
            node = stack.pop()
            result.append(node.val)
            self.push_roots(node.right, stack)

        return result

    def push_roots(self, node: TreeNode, stack: Deque) -> None:
        while node:
            stack.append(node)
            node = node.left


# recursion
class BinaryTreeInorderTraversal2:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = list()
        if not root:
            return result

        self.inorderTraversalHelper(root, result)

        return result

    def inorderTraversalHelper(
        self, node: Optional[TreeNode], result: List[int]
    ) -> None:
        if not node:
            return

        self.inorderTraversalHelper(node.left, result)
        result.append(node.val)
        self.inorderTraversalHelper(node.right, result)


# divide and conquer
class BinaryTreeInorderTraversal3:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = list()
        if not root:
            return result

        left_result = self.inorderTraversal(root.left)
        right_result = self.inorderTraversal(root.right)

        result.extend(left_result)
        result.append(root.val)
        result.extend(right_result)

        return result

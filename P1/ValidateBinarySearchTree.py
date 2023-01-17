# Tree, Depth-First Search, Binary Search Tree, Binary Tree
# Amazon 19 Bloomberg 19 Apple 5 Microsoft 4 Yahoo 3 Zillow 3 Facebook 2 Salesforce 2 Uber 2 Yandex 2 Paypal 2
# https://leetcode.com/problems/validate-binary-search-tree/
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left  subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# inorder traverse values should be increasing
class ValidateBinarySearchTree:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        iterator = InorderIterator(root)
        prev = iterator.get_next()
        while iterator.has_next():
            current = iterator.get_next()
            if prev.val >= current.val:
                return False
            else:
                prev = current

        return True


class InorderIterator:
    def __init__(self, root: TreeNode):
        self.stack = deque()
        self.push_roots(root)

    def has_next(self) -> bool:
        return self.stack

    def get_next(self) -> TreeNode:
        node = self.stack.pop()
        self.push_roots(node.right)

        return node

    def push_roots(self, root: TreeNode) -> None:
        while root:
            self.stack.append(root)
            root = root.left


class ValidateBinarySearchTree2:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        min_node = None
        max_node = None

        return self.isValidBSTHelper(root, min_node, max_node)

    def isValidBSTHelper(
        self,
        root: Optional[TreeNode],
        min_node: Optional[TreeNode],
        max_node: Optional[TreeNode],
    ):
        if not root:
            return True  # able to reach leaf means valid

        if min_node and min_node.val >= root.val:
            return False

        if max_node and max_node.val <= root.val:
            return False

        left_is_valid = self.isValidBSTHelper(root.left, min_node, root)
        right_is_valid = self.isValidBSTHelper(root.right, root, max_node)

        return left_is_valid and right_is_valid
